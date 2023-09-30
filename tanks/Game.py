from Window import Window
from Sprite import Sprite
from Tank import Tank
from Bullet import Bullet
from Constants import*
import pygame as pg
from random import randint


class Game():

    def create_objects(self):

        self.window = Window(
            WINDOW_WIDTH, WINDOW_HEIGHT,
            CAPTION, BLUE
        )


        self.tank1 = Tank(
            TANK1_X, TANK1_Y,
            TANK_WIDTH, TANK_HEIGHT,
            TANK_IMAGE_PATH
        )

        self.tank2 = Tank(
            TANK2_X, TANK2_Y,
            TANK_WIDTH, TANK_HEIGHT,
            TANK_IMAGE_PATH
        )

        self.wall1 = Sprite(V_WALL_WIDTH, V_WALL_HEIGHT, 
                       WALL1_X, WALL1_Y, 
                       WALL_IMAGE_PATH, WALL_SPEED)
        
        self.wall2 = Sprite(V_WALL_WIDTH, V_WALL_HEIGHT, 
                       WALL2_X, WALL2_Y, 
                       WALL_IMAGE_PATH, WALL_SPEED)

        self.wall3 = Sprite(H_WALL_WIDTH, H_WALL_HEIGHT, 
                       WALL3_X, WALL3_Y, 
                       WALL_IMAGE_PATH, WALL_SPEED)
        
        self.wall4 = Sprite(H_WALL_WIDTH, H_WALL_HEIGHT, 
                       WALL4_X, WALL4_Y, 
                       WALL_IMAGE_PATH, WALL_SPEED)


    def draw_objects(self):
        pass

    def move_objects(self):
        

    def collisions(self):
        pass

    def win_lose(self):
        pass

    
    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game = False

    def game_loop(self):
        self.game = True
        self.finish = False

        self.create_objects()

        while self.game:
            if self.finish: 
                self.window.screen.blit(self.final_text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
            else:
                self.draw_objects()
                self.move_objects()
                self.collisions()
                self.event_handler()
                self.win_lose()