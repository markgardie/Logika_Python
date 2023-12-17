from Sprite import*
from Constants import*
from random import randint


class Enemy(Sprite):

    def move(self):
        self.rect.y += self.speed


    def update(self):
        self.move()
