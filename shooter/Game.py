import pygame as pg
from random import randint
from Constants import*
from Enemy import*
from Player import*
from Window import*

class Game():

    def create_objects(self):

        pass

    def create_enemy(self):
        pass

    def draw_objects(self):
        pass

    def move_objects(self):
        pass

    def collisions(self):
        
        pass

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