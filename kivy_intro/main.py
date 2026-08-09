from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy import platform
from kivy.lang import Builder
from kivy.utils import hex_colormap, colormap
from kivy.metrics import sp, dp


class MenuScreen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)

    def go_game(self):
        self.manager.current = "game"
        self.manager.transition.direction = "left"

    def go_settings(self):
        self.manager.current = "settings"
        self.manager.transition.direction = "up"

    def exit_game(self):
        App.get_running_app().stop()

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    #return menu
    def goMenu(self, *args):
        self.manager.current = "menu"
        self.manager.transition.direction = "down"


class GameScreen(Screen):
    score = NumericProperty(0)

    def on_pre_enter(self, *args):
        self.score = 0
        app.LEVEL = 0
        self.ids.level_complete_oppacity = 0
        self.ids.fish.fish_index = 0

        return super().on_pre_enter(*args)

    def on_enter(self, *args):
        self.start_game()

        return super().on_enter(*args)

    def start_game(self):
        self.ids.fish.new_fish()

    def level_complete(self, *args):
        self.ids.level_complete.opacity = 1

    def go_home(self):
        self.manager.current = "menu"
        self.manager.transition.direction = "right"


class Fish(Image):
    fish_current = None
    fish_index = 0
    hp_current = None

    def on_kv_post(self, base_widget):
        self.GAME_SCREEN = self.parent.parent.parent
        return super().on_kv_post(base_widget)

    def new_fish(self, *args):
        self.fish_current = app.LEVELS[self.fish_index]

        self.source = app.FISHES[self.fish_current]["source"]

        self.hp_current = app.FISHES[self.fish_current]["hp"]

        self.opacity = 1

    def defeated(self):
        self.opacity = 0
        
    def on_touch_down(self, touch):
        if not  self.collide_point(*touch.pos) or not self.opacity:
            return
        
        self.hp_current -= 1
        
        self.GAME_SCREEN.score += 1
        
        if self.hp_current <=0:
            self.defeated()
            
            if len(app.LEVELS[app.LEVEL]) > self.fish_index + 1:
                self.fish_index += 1
                
                Clock.shedule_once(self.new_fish(), 1.2)
                
            else:
                Clock.shedule_once(self.GAME_SCREEN.level_complete, 1.2)
                
                self.fish_index = 0
                
        return super().on_touch_down(touch)


class ClickerApp(App):
    LEVEL = 0

    FISHES = {
        'fish1':
            {'sourse':"assets/images/fish01.png","hp": 5},
        'fish2':
            {'sourse': "assets/images/fish02.png", "hp": 10}
    }

    LEVELS = [
        ["fish1", "fish1", "fish2"]
    ]

    def build(self):
        sm = ScreenManager()

        sm.add_widget(Menu(name = "menu"))
        sm.add_widget(Settings(name = "settings"))
        sm.add_widget(Game(name = "game"))

        return sm

if platform != "android":
    Window.size = (450, 900)

app = ClickerApp()
app.run()
