from Sprite import Sprite
import pygame as pg
from Constants import*
from Bullet import Bullet

class Tank(Sprite):


    def fire1(self, bullets1):
        bullet = Bullet(
            BULLET_WIDTH, BULLET_HEIGHT,
            self.hitbox.right, self.hitbox.centery,
            BULLET_IMAGE_PATH, BULLET_SPEED
        )

        bullets1.append(bullet)