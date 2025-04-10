from constants import*
from sprite import Sprite
from window import Window
from ball import Ball
from my_platform import Platform
from random import randint
import pygame as pg

class Game():

    def create_objects(self):
        pg.font.init()
        self.main_window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE)

        self.main_ball = Ball(BALL_WIDTH, BALL_HEIGHT, 
                              WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 
                              BALL_IMAGE_PATH)
        
        self.main_platform = Platform(PLATFORM_WIDTH, PLATFORM_HEIGHT, 
                                 WINDOW_WIDTH / 2, WINDOW_HEIGHT - 100,
                                 PLATFORM_IMAGE_PATH)
    
        self.blocks = []
        self.create_blocks()

                
        self.dir_x = 1
        self.dir_y = -1
        

    def create_blocks(self):
        x = 20
        y = 20

        for row in MAP:
            for cell in row:
                if cell == "1":
                    block = Sprite(BLOCK_WIDTH, BLOCK_HEIGHT, x, y, BLOCK_IMAGE_PATH)
                    self.blocks.append(block)
                x += 76
            y += 56
            x = 20    

    def draw_objects(self):
        self.main_window.background.fill(BLUE)
        self.main_window.background.blit(
            self.main_platform.image,
            (self.main_platform.hitbox.x, self.main_platform.hitbox.y)
        )

        self.main_window.background.blit(
            self.main_ball.image,
            (self.main_ball.hitbox.x, self.main_ball.hitbox.y)
        )

        for block in self.blocks:
            self.main_window.background.blit(
            block.image,
            (block.hitbox.x, block.hitbox.y)
        )

    def move_objects(self):


        self.main_ball.move(self.dir_x, self.dir_y)
        self.main_platform.controls(pg.K_a, pg.K_d)

    def collisions(self):
        for block in self.blocks:
            if self.main_ball.hitbox.colliderect(block.hitbox):
                self.dir_y = 1
                self.dir_x = randint(-1, 1)
                self.blocks.remove(block)

        if self.main_ball.hitbox.colliderect(self.main_platform.hitbox):
            self.dir_y = -1
            self.dir_x = randint(-1, 1)

        if self.main_ball.hitbox.x > WINDOW_WIDTH:
            self.dir_x = -1

        if self.main_ball.hitbox.x < 0:
            self.dir_x = 1

        if self.main_ball.hitbox.y < 0:
            self.dir_y = 1

    def win_lose(self):
        font = pg.font.Font(None, FONT_SIZE)

        if len(self.blocks) == 0:
            self.finish = True
            self.text = font.render(WIN_TEXT, True, BLACK)

        if self.main_ball.hitbox.y > WINDOW_HEIGHT:
            self.finish = True
            self.text = font.render(LOSE_TEXT, True, BLACK)

    def update_window(self):
        self.main_window.clock.tick(60)
        pg.display.update()

    def event_handler(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.game = False

    def game_loop(self):
        self.create_objects()
        self.game = True
        self.finish = False

        while self.game:
            self.event_handler()
            self.update_window()
            if self.finish:
                self.main_window.background.blit(
                    self.text,
                    (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
                )
            else:
                self.draw_objects()
                self.move_objects()
                self.collisions()
                self.win_lose()
                

Game().game_loop()