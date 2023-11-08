from typing import Any
from Sprite import Sprite
from Constants import*

class Bullet(Sprite):

    def move(self):
        self.rect.y -= self.speed

    def update(self):
        self.move()