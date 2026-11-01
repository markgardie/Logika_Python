from sprite import Sprite
import pygame as pg
from constants import WINDOW_WIDTH, PLATFORM_WIDTH

class Player(Sprite):

    # dz: керування
    def update(self, key_left, key_right):
        keys = pg.key.get_pressed()

        if keys[key_left] and self.rect.x > 0:
            self.rect.x -= self.speed

        if keys[key_right] and self.rect.x < WINDOW_WIDTH - PLATFORM_WIDTH:
            self.rect.x += self.speed