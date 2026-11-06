from sprite import Sprite
import pygame as pg
from constants import WINDOW_WIDTH


class Player(Sprite):

    # Керування платформою
    def update(self, key_left, key_right):
        keys = pg.key.get_pressed()

        if keys[key_left]:
            self.rect.x -= self.speed

        if keys[key_right]:
            self.rect.x += self.speed

        # Перевірка меж вікна
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH