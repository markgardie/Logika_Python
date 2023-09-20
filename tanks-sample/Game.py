from Window import Window
from Sprite import Sprite
from Platform import Platform
from Ball import Ball
from Constants import*
import pygame as pg
from random import randint

class Game():

    def create_objects(self):

      pass
    
   
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
        pass

    def move_objects(self):

        pass

    def collisions(self):
        
        pass

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game = False

    def win_lose(self):

        font = pg.font.Font(None, FONT_SIZE)

        if #TODO:
            self.finish = True
            self.final_text = font.render(WIN_TEXT, True, BLACK)

        if #TODO:
            self.finish = True
            self.final_text = font.render(LOSE_TEXT, True, BLACK)

