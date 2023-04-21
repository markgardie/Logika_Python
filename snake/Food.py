from Sprite import*
from random import*
from constants import*

class Food(Sprite):

    def move(self):
        self.hitbox.x = randint(10, WINDOW_WIDTH - 10)
        self.hitbox.y = randint(10, WINDOW_HEIGHT - 10)

    