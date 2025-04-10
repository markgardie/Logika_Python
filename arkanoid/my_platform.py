from sprite import Sprite
import pygame as pg
from constants import*

PLATFORM_SPEED = 10

class Platform(Sprite):

    def controls(self, left_key, right_key):
        keys = pg.key.get_pressed()

        if keys[left_key] and self.hitbox.x > 0:
            self.hitbox.x -= PLATFORM_SPEED

        if keys[right_key] and self.hitbox.x < WINDOW_WIDTH:
            self.hitbox.x += PLATFORM_SPEED
