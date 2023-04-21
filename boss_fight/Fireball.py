from Sprite import*
from random import randint

class Fireball(Sprite):

    def move(self, direction_x, direction_y):
       

        self.hitbox.x -= self.speed * direction_x
        self.hitbox.y -= self.speed * direction_y