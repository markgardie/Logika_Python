from sprite import Sprite
from constants import*
import pygame as pg

class Cell(Sprite):

    def __init__(self, width, height, start_image_path, cross_image_path, zero_image_path, x, y):
        super().__init__(width, height, start_image_path, x, y)

        self.cross_image = pg.image.load(cross_image_path)
        self.cross_image = pg.transform.scale(self.cross_image, (width, height))

        self.zero_image = pg.image.load(zero_image_path)
        self.zero_image = pg.transform.scale(self.zero_image, (width, height))

        self.filled = 0

    def click(self, player_id):
        if self.filled == 0:
            if player_id == 1:
                self.image = self.cross_image
                self.filled = 1
            else:
                self.image = self.zero_image
                self.filled = 2
            

    
