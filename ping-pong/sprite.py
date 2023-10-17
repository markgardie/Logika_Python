import pygame as pg

class Sprite():

    def __init__(self, width, height, image_path, x, y):

        self.rect = pg.Rect(x, y, width, height)

        self.image = pg.image.load(image_path)
        self.image = pg.transform.scale(self.image, (width, height))