import pygame as pg
from random import randint
from Constants import*
from Enemy import*
from Player import*
from Window import*

class Game():

    def create_objects(self):
        self.bullets = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.create_enemy()
        self.window = Window()
        self.player = Player()

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
        self.bullets.draw(self.window.screen)
        self.enemies.draw(self.window.screen)
        self.player.draw(self.window.screen)


    def move_objects(self):
        self.bullets.update()
        self.enemies.update()
        self.player.controls()

    def collisions(self):
        collides = pg.sprite.groupcollide(self.enemies, self.bullets, True, True)

        for c in collides:
            self.scores += 1
            self.create_enemy()
        
        for enemy in self.enemies.sprites():
            if enemy.y > WINDOW_WIDTH + 10 or enemy.rect.colliderect(self.player.rect):
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
            
            
    def update_window(self):
        pg.display.update()
        self.window.clock.tick(FPS)

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