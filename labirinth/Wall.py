import pygame as pg

pg.init()

class Wall(pg.sprite.Sprite):
    def __init__(self, color1, color2, color3, x, y, width, heigth):
        super().__init__()

        self.image = pg.Surface((width, heigth))
        self.image.fill((color1, color2, color3))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y