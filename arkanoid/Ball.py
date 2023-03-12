from Sprite import*
from constants import*

class Ball(Sprite):

    def move(self, direction_x, direction_y):
        self.hitbox.x -= BALL_SPEED * direction_x
        self.hitbox.y -= BALL_SPEED * direction_y
