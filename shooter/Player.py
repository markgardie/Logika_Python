from Sprite import Sprite
from Bullet import Bullet
from constants import*

class Player(Sprite):

    def controls(self, left, right, up, down):
        pass

    def fire(self, bullets):
        bullet = Bullet(
            BULLET_WIDTH, BULLET_HEIGHT,
            BULLET_X, BULLET_Y,
            BULLET_IMAGE_PATH
        )
        bullets.add(bullet)