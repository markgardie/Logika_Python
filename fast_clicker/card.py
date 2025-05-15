import pygame as pg
from sprite import Sprite
from constants import *

class Card(Sprite):

    def __init__(self, width, height, x, y, color):
        super().__init__(width, height, x, y)
        self.color = color
        self.font = pg.font.Font(None, TEXT_SIZE)
        self.text = self.font.render(TEXT, True, TEXT_COLOR)

    def set_color(self, new_color):
        self.color = new_color