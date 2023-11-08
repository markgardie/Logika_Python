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
                             PLAYER_IMAGE_PATH, PLAYER_SPEED)
        
        self.bullets = pg.sprite.Group()
        
        self.create_enemies()

        self.miss = 0
        self.scores = 0

        self.create_counters()

    def create_counters(self):
        self.scores_text = FONT.render(f"{SCORES_TEXT} {self.scores}", True, BLACK)
        self.miss_text = FONT.render(f"{MISS_TEXT} {self.miss}", True, BLACK)

    def create_enemies(self):
        self.enemies = pg.sprite.Group()

        for i in range(ENEMY_NUMBER):
            self.generate_enemy()

    def draw_objects(self):
        self.window.screen.blit(self.window.image, (0, 0))
        self.window.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
       
        self.window.screen.blit(self.scores_text, SCORES_TEXT_COR)
        self.window.screen.blit(self.miss_text, MISS_TEXT_COR)
       
        self.enemies.draw(self.window.screen)
        self.bullets.draw(self.window.screen)


    def move_objects(self):
        self.player.controls(pg.K_a, pg.K_d, pg.K_w, pg.K_s)
        self.enemies.update()
        self.bullets.update()
        
    def collisions(self):
        
        collides = pg.sprite.groupcollide(self.enemies, self.bullets, True, True)

        for collide in collides:
            self.scores += 1
            self.generate_enemy()
          

        for enemy in self.enemies:
            if (enemy.rect.y > WINDOW_HEIGHT - 5
                or enemy.rect.colliderect(self.player.rect)):
                self.miss += 1
                enemy.kill()
                self.generate_enemy()

    def generate_enemy(self):

        x = randint(ENEMY_X_START, ENEMY_X_END)
        speed = randint(1, 5)
            
        enemy = Enemy(ENEMY_WIDTH, ENEMY_HEGHT, 
                          x, ENEMY_Y,
                          ENEMY_IMAGE_PATH, speed)
            
        self.enemies.add(enemy)

    def win_lose(self):
        
        if self.scores >= GOAL:
            self.finish = True
            self.text = FONT.render(WIN_TEXT, True, BLACK)

        if self.miss >= MAX_MISS:
            self.finish = True
            self.text = FONT.render(LOSE_TEXT, True, BLACK)
        
    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game = False
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.player.fire(self.bullets)

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
                self.event_handler()
                self.update_window()
            else:
                self.create_counters()
                self.draw_objects()
                self.move_objects()
                self.collisions()
                self.win_lose()
                self.update_window()
                self.event_handler()

Game().game_loop()