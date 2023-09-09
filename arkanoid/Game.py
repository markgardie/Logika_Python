from Window import Window
from Sprite import Sprite
from Platform import Platform
from Ball import Ball
from Constants import*
import pygame as pg
from random import randint

class Game():

    def create_objects(self):

        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE)

        self.platform = Platform(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 30, 
                                 PLATFORM_WIDTH, PLATFORM_HEIGHT,
                                 PLATFORM_IMAGE_PATH)
        
        self.ball = Ball(WINDOW_WIDTH / 2, WINDOW_HEIGHT /2, 
                                 BALL_WIDTH, BALL_HEIGHT,
                                 BALL_IMAGE_PATH)
        
        self.blocks = self.create_blocks()
    
    def create_blocks(self):
        blocks = []

        x = 20
        y = 20

        for row in MAP:
            for place in row:
                if place == "1":
                    block = Sprite(x, y, BLOCK_WIDTH, BLOCK_HEIGHT, BLOCK_IMAGE_PATH)
                    blocks.append(block)

                x += 76

            y += 56
            x = 20

        
        return blocks
    
    def game_loop(self):

        self.game = True
        self.finish = False

        while self.game:
            if self.finish: 
                self.window.screen.blit(self.final_text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
            else:
                self.draw_objects()
                self.move_objects()
                self.collisions()
                self.event_handler()
                self.win_lose()

    def draw_objects(self):
        self.window.screen.blit(self.platform.image, (self.platform.hitbox.x, self.platform.hitbox.y))
        self.window.screen.blit(self.ball.image, (self.ball.hitbox.x, self.ball.hitbox.y))

        for block in self.blocks:
            self.window.screen.blit(block.image, (block.hitbox.x, block.hitbox.y))

    def move_objects(self):

        self.dir_x = 1
        self.dir_y = -1

        self.platform.controls(pg.K_a, pg.K_d)
        self.ball.move(self.dir_x, self.dir_y)

    def collisions(self):
        
        # ball, platform
        if self.ball.hitbox.colliderect(self.platform.hitbox):
            self.dir_y = -1
            self.dir_x = randint(-1, 1)

        # ball, blocks
        for block in self.blocks:
            if self.ball.hitbox.colliderect(self.block.hitbox):
                self.dir_y = 1
                self.dir_x = randint(-1, 1)

        # ball, left border
        if self.ball.hitbox.x < 0:
            self.dir_x = 1

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game = False

    def win_lose(self):

        font = pg.font.Font(None, FONT_SIZE)

        if len(self.blocks) == 0:
            self.finish = True
            self.final_text = font.render(WIN_TEXT, True, BLACK)

        if self.ball.hitbox.y > WINDOW_HEIGHT:
            self.finish = True
            self.final_text = font.render(LOSE_TEXT, True, BLACK)

