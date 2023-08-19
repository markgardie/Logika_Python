from Sprite import*
from Constants import*

class Platform(Sprite):

    def controls(self, left, right):

        key_pressed = pg.key.get_pressed()

        if key_pressed[left] and self.hitbox.x > 0:
            self.hitbox.x -= PLATFORM_SPEED

        # right - homework