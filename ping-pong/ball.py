from sprite import Sprite
from constants import*

class Ball(Sprite):

    def move(self, dir_x, dir_y):
        self.rect.x += BALL_SPEED * dir_x
        self.rect.y += BALL_SPEED * dir_y