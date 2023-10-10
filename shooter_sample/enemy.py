from sprite import*
from constants import*
from random import randint

class Enemy(Sprite):

    
    def update(self):
        self.rect.y += self.speed

        if self.rect.y > WINDOW_HEIGHT:
            
            miss[0] += 1
            self.rect.x = randint(80, WINDOW_WIDTH - 80)
            self.rect.y = 0