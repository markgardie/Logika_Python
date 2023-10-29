from Sprite import Sprite
from Constants import*

class Enemy(Sprite):

    def move(self):
        self.rect.y += ENEMY_SPEED
