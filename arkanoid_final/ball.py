from sprite import Sprite
from random import choice
from constants import WINDOW_WIDTH


class Ball(Sprite):

    def __init__(self, coords, size, speed, image_path):
        super().__init__(coords, size, speed, image_path)

        self.dir_x = choice([-1, 1])
        self.dir_y = -1

    def update(self):
        self.rect.x += self.speed * self.dir_x
        self.rect.y += self.speed * self.dir_y

    # Перевірка зіткнення зі стінами
    def collisions(self):

        # Ліва стіна
        if self.rect.left <= 0:
            self.rect.left = 0
            self.dir_x = 1

        # Права стіна
        if self.rect.right >= WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
            self.dir_x = -1

        # Верхня стіна
        if self.rect.top <= 0:
            self.rect.top = 0
            self.dir_y = 1