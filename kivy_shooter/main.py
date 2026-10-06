from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.core.window import Window
from kivy import platform
from kivy.uix.image import Image
from random import randint
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Keyboard
from kivy.properties import NumericProperty
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.fitimage import FitImage
from particles import Particle


FPS = 30
BULLET_SPEED = dp(600)
SHIP_SPEED = dp(300)
SHIP_SPEED_FORWARD = dp(180)
DIR_UP = 1
DIR_DOWN = -1

SPAWN_ENEMY_TIME = 2

HP_DEF = 3

FIRE_RATE_MIN = 0.5
FIRE_RATE_MEDIUM = 2
FIRE_RATE_DEF = FIRE_RATE_MIN

class Shot(MDWidget):
    def __init__(self, direction, owner, **kwargs):
        super().__init__(**kwargs)
        self.direction = direction
        self.owner = owner

class MainScreen(MDScreen):
    ...

class Ship(Image):
    hp = NumericProperty()
    max_hp = NumericProperty()

    def __init__(self, direction = DIR_UP, hp = HP_DEF, fire_rate = FIRE_RATE_MEDIUM, **kwargs):
        super().__init__(**kwargs)
        self.direction = direction
        self.hp = self.max_hp = hp

        self.fire_rate = fire_rate
        self._last_shot = self.fire_rate

        self.anim_delay = 1 / 30
        self._last_anim = self.anim_delay
        self._current_anim = 0


    def moveLeft(self):
        self.pos[0] -= SHIP_SPEED
    
    def moveRight(self):
        self.pos[0] += SHIP_SPEED

    def shot(self):
        shot = Shot(self.direction, owner = self)
        shot.center_x = self.center_x
        shot.y = self.top if self.direction == DIR_UP else self.y - shot.height
        self.parent.parent.parent.parent.bullets.append(shot)
        self.parent.add_widget(shot)

        self._last_shot = 0

    def update(self):
        pass

class PlayerShip(Ship):
    def __init__(self, direction=DIR_UP, **kwargs):
        super().__init__(direction, **kwargs)

    def update(self, keys):
        for key in keys:
            if keys[key]:
                if key == "left" and self.center_x > 0:
                    self.moveLeft()
                if key == "right" and self.center_x < Window.width:
                    self.moveRight()
                if key == "shot":
                    self.shot()
                    keys[key] = False
    def animation(self, dt):
        if self._last_anim >= self.anim_delay:
            p = Particle(
                source = "",
                width = dp(70 + randint(0, 50)),
                y = dp(self.y + randint(-15, 0)),
                life = 0.4,
                speed = dp(200),
                direction= self.direction * -1
            )
            if self.parent:
                self.parent.add_widget(p)

            self._last_anim = 0
        self._last_anim += dt
    
class EnemyShip(Ship):
    def __init__(self, direction=DIR_DOWN, **kwargs):
        super().__init__(direction, **kwargs)
        self.frame = 0

    def update(self):
        super().update()
        self.pos[1] -= dp(3)
        if self.frame % 100 == 0:
            self.shot()
        self.frame += 1

    def animation(self, dt):
        if self._last_anim >= self.anim_delay:
            p = Particle(
                source = "",
                width = dp(50 + randint(0, 50)),
                y = dp(self.y + randint(-15, 0)),
                life = 0.3,
                speed = 0,
                direction= self.direction * -1,
                opacity = 1
            )
            if self.parent:
                self.parent.add_widget(p)

            self._last_anim = 0
        self._last_anim += dt

class MoveBackground(MDFloatLayout):
    def __init__(self, source, speed = dp(1), scale = 1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = speed
        self.add_widget(FitImage(source = source, size_hint_y = scale))
        self.add_widget(FitImage(
            source = source, 
            size_hint_y = scale, 
            pos = (0, Window.size[1]) * scale))

    def move(self):
        for img in self.children:
            img.pos[1] -= self.speed
            if img.top <= 0:
                img.pos[1] = img.size[1]

class GameScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.eventkeys = {}
        self.enemyShips = []
        self.bullets = []

        self.ship = self.ids.ship

        self.pauseMenu = None

        self.spawn_delay = SPAWN_ENEMY_TIME
        self.time_last_spawn = 0

        self.backBack = MoveBackground(source="", speed = 0.5)
        self.backFront = MoveBackground(source="", speed = 1, scale = 3)

        self.ids.back.add_widget(self.backBack)
        self.ids.back.add_widget(self.backFront)

        # desktop
        Window.bind(on_key_down = self._on_key_down)
        Window.bind(on_key_up = self._on_key_up)

    def on_enter(self, *args):
        self.updateEvent = Clock.schedule_interval(self.update, 1 / FPS)
        self.ship = self.ids.ship

        return super().on_enter(*args)

    # dz
    def spawn_enemy(self):
        pass

    def update(self, dt):
        self.ship.update(self.eventkeys)

        self.time_last_spawn += dt
        if self.time_last_spawn >= self.spawn_delay:
            self.spawn_enemy()
            self.time_last_spawn = 0

        for enemy in self.enemyShips:
            enemy.update()
            if enemy.top < 0:
                self.enemyShips.remove(enemy)
                self.ids.front.remove_widget(enemy)

            if enemy.collide_widget(self.ship):
                self.game_over()

        self.manage_bullets()

        self.backBack.move()
        self.backFront.move()

    # dz
    def manage_bullets(self):
        pass

    def check_collisions(self, bullet):
        if bullet.owner == self.ship:
            for enemy in self.enemyShips:
                if bullet.collide_widget(enemy):
                    self.enemyShips.remove(enemy)
                    self.ids.front.remove_widget(enemy)

                    self.remove_bullets(bullet)
                    break
        else:
            if bullet.collide_widget(self.ship):
                self.game_over()
                self.remove_bullets(bullet)

    # dz
    def remove_bullets(self, bullet):
        pass

    def game_over(self):
        self.updateEvent.cancel()
        for enemy in self.enemyShips:
            self.enemyShips.remove(enemy)
            self.ids.front.remove_widget(enemy)
        # remove bullets: dz

        self.manager.current = "game_over"

    def pressKey(self, key):
        self.eventkeys[key] = True

    def releaseKey(self, key):
        self.eventkeys[key] = False

    def show_menu(self):
        self.updateEvent.cancel()

        if not self.pauseMenu:
            self.pauseMenu = MDDialog(
                title = "Game Paused",
                text = "Resume the game?",
                on_dismiss = self.resumeGame,
                buttons = [
                    MDFlatButton(
                        text = "RESUME",
                        theme_text_color = "Custom",
                        text_color = app.theme_cls.primary_color,
                        on_press = self.pauseStop
                    )
                ]

            )
        self.pauseMenu.open()

    def pauseStop(self, *args):
        self.pauseMenu.dismiss()

    def resumeGame(self, *args):
        self.updateEvent = Clock.schedule_interval(self.update, 1 / FPS)

    def _on_key_down(self, window, keycode, *args, **kwargs):
        key = key if (key := Keyboard.keycode_to_string(window, keycode)) != "spacebar" else "shot"
        self.eventkeys[key] = True

    # dz
    def _on_key_up(self, window, keycode, *args, **kwargs):
        pass
    

class ShooterApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        self.sm = MDScreenManager()

        self.sm.add_widget(MainScreen(name = "main"))
        self.sm.add_widget(GameScreen(name = "game"))

        return self.sm

if platform != "android":
    Window.size = (450, 900)
    Window.top = 100
    Window.left = 600

app = ShooterApp()
app.run()