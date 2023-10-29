import pygame as pg
from Sprite import Sprite
from Window import Window
from Player import Player
from Enemy import Enemy
from Constants import *
from random import randint

class Game():

    def create_objects(self):
        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BACKGROUND_IMAGE_PATH)
        self.player = Player(PLAYER_WIDTH, PLAYER_HEIGHT,
                             PLAYER_X, PLAYER_Y,
                             PLAYER_IMAGE_PATH)
        
        self.create_enemies()

    def create_enemies(self):
        self.enemies = pg.sprite.Group()

        for i in range(ENEMY_NUMBER):
            x = randint(ENEMY_X_START, ENEMY_X_END)
            speed = randint(1, 5)
            
            enemy = Enemy(ENEMY_WIDTH, ENEMY_HEGHT, 
                          x, ENEMY_Y,
                          ENEMY_IMAGE_PATH, speed)
            
            self.enemies.add(enemy)


    def draw_objects(self):
        self.window.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        self.enemies.draw(self.window.screen)

    def move_objects(self):
        self.player.controls(pg.K_a, pg.K_d, pg.K_w, pg.K_s)
        self.enemies.update()

        
    def collisions(self):
        
        pass

    def win_lose(self):
        pass
        

    def update_window(self):
        self.window.clock.tick(FPS)
        pg.display.update()

    def game_loop(self):
        self.create_objects()
        self.game = True
        self.finish = False

        while self.game:
            if self.finish:
                self.window.screen.blit(self.text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
            else:
                self.draw_objects()
                self.move_objects()
                self.collisions()
                self.win_lose()
                self.update_window()

Game().game_loop()