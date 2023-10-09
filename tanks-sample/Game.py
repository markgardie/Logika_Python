from Window import Window
from Sprite import Sprite
from Tank import Tank
from Bullet import Bullet
from Constants import*
import pygame as pg
from random import randint

pg.font.init()

class Game():

    def create_objects(self):

        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT,CAPTION, WHITE)

        self.tank1 = Tank(TANK_WIDTH, TANK_HEIGHT, TANK1_X, TANKS_Y, TANK1_IMAGE_PATH, PLAYER_SPEED)
        self.tank2 = Tank(TANK_WIDTH, TANK_HEIGHT, TANK2_X, TANKS_Y, TANK2_IMAGE_PATH, PLAYER_SPEED)

        wall1 = Sprite(V_WALL_WIDTH, V_WALL_HEIGHT, WALL1_X, WALL1_Y, WALL_IMAGE_PATH, WALL_SPEED)
        wall2 = Sprite(V_WALL_WIDTH, V_WALL_HEIGHT, WALL2_X, WALL2_Y, WALL_IMAGE_PATH, WALL_SPEED)

        wall3 = Sprite(H_WALL_WIDTH, H_WALL_HEIGHT, WALL3_X, WALL3_Y, WALL_IMAGE_PATH, WALL_SPEED)
        wall4 = Sprite(H_WALL_WIDTH, H_WALL_HEIGHT, WALL4_X, WALL4_Y, WALL_IMAGE_PATH, WALL_SPEED)

        self.bullets1 = []
        self.bullets2 = []

        self.walls = [wall1, wall2, wall3, wall4]

    
    def draw_objects(self):
        self.window.screen.blit(self.tank1.image, (self.tank1.hitbox.x, self.tank1.hitbox.y))
        self.window.screen.blit(self.tank2.image, (self.tank2.hitbox.x, self.tank2.hitbox.y))
        self.draw_bullets()
        self.draw_walls()

        
    def draw_walls(self):
        for wall in self.walls:
            self.window.screen.blit(wall.image, (wall.hitbox.x, wall.hitbox.y))

    def draw_bullets(self):
        for bullet in self.bullets1:
            self.window.screen.blit(bullet.image, (bullet.hitbox.x, bullet.hitbox.y))
    
        for bullet in self.bullets2:
            self.window.screen.blit(bullet.image, (bullet.hitbox.x, bullet.hitbox.y))


    def move_objects(self):

        self.move_bullets()

        self.tank1.controls(pg.K_a, pg.K_d, pg.K_w, pg.K_s)
        self.tank2.controls(pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN)

    def move_bullets(self):
        for bullet in self.bullets1:
            bullet.move(1)
    
        for bullet in self.bullets2:
            bullet.move(-1)

    def collisions(self):
        
        for wall in self.walls:

            for bullet in self.bullets1:
                if bullet.hitbox.colliderect(wall.hitbox):
                    self.bullets1.remove(bullet)
                    
            for bullet in self.bullets2:
                if bullet.hitbox.colliderect(wall.hitbox):
                    self.bullets2.remove(bullet)

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game = False
            if event.type == pg.KEYDOWN and event.key == pg.K_e:
                self.tank1.fire1(self.bullets1)
            if event.type == pg.KEYDOWN and event.key == pg.K_l:
                self.tank2.fire2(self.bullets2)

    def win_lose(self):

        font = pg.font.Font(None, 50)

        for bullet in self.bullets1:
            if self.tank2.hitbox.colliderect(bullet.hitbox):
                self.finish = True
                self.final_text = font.render("Переміг гравець 1", True, BLACK)

        for bullet in self.bullets2:
            
            if self.tank1.hitbox.colliderect(bullet.hitbox):
                self.finish = True
                self.final_text = font.render("Переміг гравець 2", True, BLACK)

        for wall in self.walls:
            
            if self.tank1.hitbox.colliderect(wall.hitbox):
                self.finish = True
                self.final_text = font.render("Переміг гравець 2", True, BLACK)

            if self.tank2.hitbox.colliderect(wall.hitbox):
                self.finish = True
                self.final_text = font.render("Переміг гравець 1", True, BLACK)

        if self.tank1.hitbox.colliderect(self.tank2.hitbox):
                self.finish = True
                self.final_text = font.render("Нічия", True, BLACK)

    
    def update_window(self):
        pg.display.flip()
        self.window.screen.fill(WHITE)
        self.window.clock.tick(FPS)
        

    def game_loop(self):
        self.create_objects()

        self.game = True
        self.finish = False

        while self.game:
            if not self.finish: 
                self.draw_objects()
                self.move_objects()
                self.collisions()
                self.event_handler()
                self.win_lose()
                self.update_window()
            else:
                self.window.screen.blit(self.final_text, (WINDOW_WIDTH / 2 - 150, WINDOW_HEIGHT / 2 - 100))
                self.update_window()
                self.event_handler()
                


Game().game_loop()