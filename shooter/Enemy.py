from Sprite import*
from random import randint
from constants import*

class Enemy(Sprite):

    def move(self):
        
        self.hitbox.y += self.speed

        if self.hitbox.y > WINDOW_HEIGHT:
            x = randint(100, WINDOW_WIDTH - 100)
            self.hitbox.x = x
            self.hitbox.y = ENEMY_Y

            miss[0] += 1

    def update(self):
        self.move()
