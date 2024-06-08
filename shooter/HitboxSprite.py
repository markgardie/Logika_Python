import pygame as pg

class HitboxSprite(pg.sprite.Sprite):

    def __init__(self, x, y, width, height, image_path):
        self.rect = pg.Rect(x, y, width, height)

        self.image = pg.image.load(image_path)
        self.image = pg.transform.scale(self.image, (width, height))

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))