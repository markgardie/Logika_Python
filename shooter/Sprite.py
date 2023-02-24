import pygame as pg


class Sprite(pg.sprite.Sprite):
    def __init__(self, width, height, x, y, image_path, speed):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.transform.scale(pg.image.load(image_path), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
