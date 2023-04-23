from Sprite import*
from random import*
from constants import*

class Food(Sprite):

    def move(self):
        self.hitbox.x = randint(50, WINDOW_WIDTH - 50)
        self.hitbox.y = randint(50, WINDOW_HEIGHT - 50)