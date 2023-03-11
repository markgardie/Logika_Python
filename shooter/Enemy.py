from Sprite import*
from random import randint
from constants import*

class Enemy(Sprite):

    def move(self):
        
        self.rect.y += self.speed

        if self.rect.y > WINDOW_HEIGHT:
            x = randint(100, WINDOW_WIDTH - 100)
            self.rect.x = x
            self.rect.y = ENEMY_Y

            miss[0] += 1

    def update(self):
        self.move()
