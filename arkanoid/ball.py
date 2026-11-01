from sprite import Sprite
from random import randint
from constants import WINDOW_WIDTH

class Ball(Sprite):

    def __init__(self, coords, size, speed, image_path):
        super().__init__(coords, size, speed, image_path)
        self.dir_x = randint(-1, 1)
        self.dir_y = -1

    def update(self):
        self.rect.x += self.speed * self.dir_x
        self.rect.y += self.speed * self.dir_y

    def collisions(self):
        if self.rect.x <= 0 or self.rect.x >= WINDOW_WIDTH:
            self.dir_x *= -1

        if self.rect.y <= 0:
            self.dir_y = 1
