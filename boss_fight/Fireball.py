from Sprite import*
from random import randint

class Fireball(Sprite):

    def __init__(self, width, height, x, y, image_path, speed, dir_x, dir_y):
        
        super().__init__(width, height, x, y, image_path, speed)

        self.dir_x = dir_x
        self.dir_y = dir_y

    def move(self):
       

        self.hitbox.x += self.speed * self.dir_x
        self.hitbox.y += self.speed * self.dir_y