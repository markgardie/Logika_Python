from typing import Any
from Sprite import Sprite
from Constants import*
from random import randint

class Enemy(Sprite):

    # постійний, автоматичний рух ворогів вниз
    def move(self):
        self.rect.y += self.speed

    def update(self):
        self.move()
