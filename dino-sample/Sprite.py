import pygame as pg

class Sprite():

    def __init__(self, x, y, width, height, image_path, speed):
        self.hitbox = pg.Rect(x, y, width, height)

        self.image = pg.image.load(image_path)
        self.image = pg.transform.scale(self.image, (width, height))

        self.speed = speed