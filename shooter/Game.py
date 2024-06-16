import pygame as pg
from random import randint
from Constants import*
from Enemy import*
from Player import*
from Window import*

class Game():

    def create_objects(self):
        self.enemies = pg.sprite.Group()

    def create_enemy(self):
        x = randint(ENEMY_X_START, ENEMY_X_END)
        speed = randint(1, 5)

        enemy = Enemy(
                ENEMY_WIDTH, ENEMY_HEIGHT, 
                x, ENEMY_Y,
                ENEMY_IMAGE_PATH, speed
            )
        
        self.enemies.add(enemy)

    def draw_objects(self):
        self.enemies.draw(self.window.screen)


    def move_objects(self):
        self.enemies.update()


    def collisions(self):
        collides = pg.sprite.groupcollide(self.enemies, self.bullets, True, True)

        for c in collides:
            self.create_enemy()
            self.scores += 1

        for enemy in self.enemies.sprites():
            if enemy.rect.colliderect(self.player.rect):
                self.miss += 1
                enemy.kill()
                self.create_enemy()

    def win_lose(self):
       
        pass

    def event_handler(self):
        pass
            
    def update_window(self):
        pass

    def game_loop(self):
        self.create_objects()
        self.game = True
        self.finish = False

        while self.game:
            if self.finish:
                pass
            else:
                self.draw_objects()
                self.move_objects()
                self.collisions()
                self.win_lose()
                self.update_window()

Game().game_loop()