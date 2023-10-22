from Sprite import Sprite
from constants import*

class Enemy(Sprite):

    def move(self):
        self.rect.y += ENEMY_SPEED
