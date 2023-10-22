import pygame as pg

class Sprite():

    def __init__(self, width, height, x, y, image_path):
        self.hitbox = pg.Rect(x, y, width, height)

        self.image = pg.image.load(image_path)
        self.image = pg.transform.scale(self.image, (width, height))