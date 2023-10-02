import pygame as pg

class Sprite():

    def __init__(self, width, height, x, y):
        self.hitbox = pg.Rect(x, y, width, height)

        