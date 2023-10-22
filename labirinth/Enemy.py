from Sprite import Sprite
from constants import*

class Enemy(Sprite):

    def move(self):
        while self.rect.x < ENEMY_RIGHT_POINT:
            self.rect.x += ENEMY_SPEED
        
        while self.rect.x > ENEMY_LEFT_POINT:
            self.rect.x -= ENEMY_SPEED