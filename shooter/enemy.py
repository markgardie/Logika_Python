from sprite import*
from constants import*

class Enemy(Sprite):

    def move(self):
        self.rect.y += self.speed

    def update(self):
        self.move()
