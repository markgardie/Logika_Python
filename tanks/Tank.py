from Sprite import Sprite
import pygame as pg
from Constants import*
from Bullet import Bullet

class Tank(Sprite):

    def controls(self, w, a, s, d):

        key_pressed = pg.key.get_pressed()

        if key_pressed [w] and self.hitbox.y > 0: 
            self.hitbox.y -= TANK_SPEED

        if key_pressed [a] and self.hitbox.x > 0:
            self.hitbox.x -= TANK_SPEED
    
        if key_pressed [s] and self.hitbox.y < WINDOW_HEIGHT:
            self.hitbox.y += TANK_SPEED
    
        if key_pressed [d] and self.hitbox.x < WINDOW_WIDTH:
            self.hitbox.x += TANK_SPEED


    def fire1(self, bullets1):
        bullet = Bullet(
            BULLET_WIDTH, BULLET_HEIGHT,
            self.hitbox.right, self.hitbox.centery,
            BULLET_IMAGE_PATH, BULLET_SPEED
        )

        bullets1.append(bullet)