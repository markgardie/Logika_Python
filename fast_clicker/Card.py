import pygame as pg
from constants import*

pg.init()

class Card():

    def __init__(self, x, y, color, width, height):

        self.rect = pg.Rect(x, y, width, height)

        self.font = pg.font.Font(FONT, TEXT_SIZE)
        self.text = self.font.render(TEXT, True, TEXT_COLOR)
