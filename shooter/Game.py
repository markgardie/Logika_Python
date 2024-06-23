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
       if self.scores >= 5:
           self.finish = True
           self.text = FONT.render("Перемога", True, TEXT_COLOR)


    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game = False
            #  if event.type == pg.KEYDOWN and event.key == pg.K_w:

            
    def update_window(self):
        pg.display.update()
        self.window.clock.tick()


    def game_loop(self):
        self.create_objects()
        self.game = True
        self.finish = False

        while self.game:
            if self.finish:
                self.window.screen.blit(self.text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
                self.update_window()
            else:
                self.draw_objects()
                self.move_objects()
                self.collisions()
                self.win_lose()
                self.update_window()

Game().game_loop()