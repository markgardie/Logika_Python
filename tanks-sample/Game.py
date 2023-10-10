from Window import Window
from Sprite import Sprite
from Tank import Tank
from Bullet import Bullet
from Constants import*
import pygame as pg
from random import randint

pg.font.init()

class Game():

    # створюються всі об'єкти, які будуть на екрані
    def create_objects(self):

        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT,CAPTION, WHITE)

        # 2 танки-гравці
        self.tank1 = Tank(TANK_WIDTH, TANK_HEIGHT, TANK1_X, TANKS_Y, TANK1_IMAGE_PATH, PLAYER_SPEED)
        self.tank2 = Tank(TANK_WIDTH, TANK_HEIGHT, TANK2_X, TANKS_Y, TANK2_IMAGE_PATH, PLAYER_SPEED)

        # 4 стінки
        # 2 горизонтальні
        # 2 вертикальні
        wall1 = Sprite(V_WALL_WIDTH, V_WALL_HEIGHT, WALL1_X, WALL1_Y, WALL_IMAGE_PATH, WALL_SPEED)
        wall2 = Sprite(V_WALL_WIDTH, V_WALL_HEIGHT, WALL2_X, WALL2_Y, WALL_IMAGE_PATH, WALL_SPEED)

        wall3 = Sprite(H_WALL_WIDTH, H_WALL_HEIGHT, WALL3_X, WALL3_Y, WALL_IMAGE_PATH, WALL_SPEED)
        wall4 = Sprite(H_WALL_WIDTH, H_WALL_HEIGHT, WALL4_X, WALL4_Y, WALL_IMAGE_PATH, WALL_SPEED)

        # кулі поки пусті, бо не було пострілів
        self.bullets1 = []
        self.bullets2 = []

        # об'єднуємо всі стінки в один список
        self.walls = [wall1, wall2, wall3, wall4]

    # малювання об'єктів
    def draw_objects(self):
        # для малювання одинарних об'єктів використовуємо blit
        # малюємо їх картинки
        self.window.screen.blit(self.tank1.image, (self.tank1.hitbox.x, self.tank1.hitbox.y))
        self.window.screen.blit(self.tank2.image, (self.tank2.hitbox.x, self.tank2.hitbox.y))
       
        # куль і стінок багато, тому для них окремі функції
        self.draw_bullets()
        self.draw_walls()

        
    def draw_walls(self):
        # проходимось по списку стінок
        for wall in self.walls:
            # і повторюємо малювання для кожної стінки в списку
            self.window.screen.blit(wall.image, (wall.hitbox.x, wall.hitbox.y))

    # тут так само лише для куль
    # є окремо кулі першого і другого танків
    # тому два цикла
    def draw_bullets(self):
        for bullet in self.bullets1:
            self.window.screen.blit(bullet.image, (bullet.hitbox.x, bullet.hitbox.y))
    
        for bullet in self.bullets2:
            self.window.screen.blit(bullet.image, (bullet.hitbox.x, bullet.hitbox.y))


    def move_objects(self):
        
        # куль багато, тому для запуску їх руху робимо окрему функцію
        self.move_bullets()

        # керування танками
        # для першого танку - WASD
        # для другого - стрілки
        self.tank1.controls(pg.K_a, pg.K_d, pg.K_w, pg.K_s)
        self.tank2.controls(pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN)

    # тут також циклом перебераємо список куль
    def move_bullets(self):
        for bullet in self.bullets1:
            # перші кулі рухаються вправо, тому 1
            bullet.move(1)
    
        for bullet in self.bullets2:
            # кулі другого танку рухаються вліво, тому -1
            bullet.move(-1)

    # торкання об'єктів
    def collisions(self):

        # у нас є два списки: стінки і кулі
        # тому є багато комбінацій стінок і куль
        # аби перевірити всі комбінації треба використати 2 цикли
        # один зовнішній (проходить по стінкам)
        # один внутрішній (проходить по кулям)
        for wall in self.walls:

            for bullet in self.bullets1:
                # colliderect перевіряє торкання двох хітбоксів
                if bullet.hitbox.colliderect(wall.hitbox):
                    # видаляється куля, якщо вона торкнулась стінки
                    self.bullets1.remove(bullet)

            # тут так само, але куль другого танка
            for bullet in self.bullets2:
                if bullet.hitbox.colliderect(wall.hitbox):
                    self.bullets2.remove(bullet)

    # функція для перевірки подій
    def event_handler(self):
        for event in pg.event.get():
            # подія натискання на крестик
            if event.type == pg.QUIT:
                # зупиняється гра і закривається вікно
                self.game = False
            # подія натискання на клавішу e
            if event.type == pg.KEYDOWN and event.key == pg.K_e:
                # постріл першого танку
                self.tank1.fire1(self.bullets1)
            # подія натискання на клавішу l
            if event.type == pg.KEYDOWN and event.key == pg.K_l:
                # постріл другого танку
                self.tank2.fire2(self.bullets2)

    def win_lose(self):

        font = pg.font.Font(None, 50)

        # торкання другого танку і куль
        for bullet in self.bullets1:
            if self.tank2.hitbox.colliderect(bullet.hitbox):
                self.finish = True
                self.final_text = font.render("Переміг гравець 1", True, BLACK)

        # торкання першого танку і куль
        for bullet in self.bullets2:
            
            if self.tank1.hitbox.colliderect(bullet.hitbox):
                self.finish = True
                self.final_text = font.render("Переміг гравець 2", True, BLACK)

        # торкання обома танками стінок
        for wall in self.walls:
            
            if self.tank1.hitbox.colliderect(wall.hitbox):
                self.finish = True
                self.final_text = font.render("Переміг гравець 2", True, BLACK)

            if self.tank2.hitbox.colliderect(wall.hitbox):
                self.finish = True
                self.final_text = font.render("Переміг гравець 1", True, BLACK)

        # взаємне торкання першого і другого танку
        # один з одним
        if self.tank1.hitbox.colliderect(self.tank2.hitbox):
                self.finish = True
                self.final_text = font.render("Нічия", True, BLACK)

    
    def update_window(self):
        # оновлення екрана
        pg.display.flip()
        # заливка фона
        self.window.screen.fill(WHITE)
        # тіки годинника для оновлення вікна та кадрів
        self.window.clock.tick(FPS)
        
    # ігровий цикл
    def game_loop(self):
        self.create_objects()

        # змінна, яка відповідає за роботу гри
        self.game = True
        # змінна, яка вказує на перемикання на фінальний екран
        self.finish = False

        while self.game:
            # якщо не фініш
            if not self.finish: 
                # запускаємо основний ігровий екран
                self.draw_objects()
                self.move_objects()
                self.collisions()
                self.event_handler()
                self.win_lose()
                self.update_window()
            else:
                # в іншому випадку
                # запускаємо фінальний екран
                self.window.screen.blit(self.final_text, (WINDOW_WIDTH / 2 - 150, WINDOW_HEIGHT / 2 - 100))
                self.update_window()
                self.event_handler()
                


Game().game_loop()