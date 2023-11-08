import pygame as pg

class Sprite(pg.sprite.Sprite):

    def __init__(self, width, height, x, y, image_path, speed):

        pg.sprite.Sprite.__init__(self)

        self.rect = pg.Rect(x, y, width, height)

        self.image = pg.image.load(image_path)
        self.image = pg.transform.scale(self.image, (width, height))
        
        self.speed = speed