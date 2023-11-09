from Sprite import Sprite
from Constants import*
import pygame as pg

class Player(Sprite):

    def controls(self, left, right, up, down):
        keys = pg.key.get_pressed()

        if keys[left] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[right] and self.rect.x < WINDOW_WIDTH - 5:
            self.rect.x += self.speed

        if keys[up] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[down] and self.rect.y < WINDOW_HEIGHT - 5:
            self.rect.y += self.speed 