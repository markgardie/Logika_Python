from sprite import Sprite

BALL_SPEED = 5


class Ball(Sprite):

    def move(self, dir_x, dir_y):
        self.hitbox.x += BALL_SPEED * dir_x
        self.hitbox.y += BALL_SPEED * dir_y
