from sprite import*
from constants import*
from bullet import*
import pygame as pg

class Player(Sprite):

    def controls(self, left, right):

        keys = pg.event.get_pressed()

        if keys[right] and self.rect.x < WINDOW_WIDTH - 10:
            self.rect.x += self.speed

        