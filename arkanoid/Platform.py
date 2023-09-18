from Sprite import*
from Constants import*

class Platform(Sprite):
    
    def controls(self, left, right):

        keys = pg.key.get_pressed()

        if keys[left] and self.hitbox.x > 0:
            self.hitbox.x -= PLATFORM_SPEED