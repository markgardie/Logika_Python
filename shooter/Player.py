from Sprite import*
from Constants import*
from Bullet import*

class Player(Sprite):

    
    def controls(self, left, right):
        keys = pg.key.get_pressed()

        if keys[left] and self.hitbox.x > 5:
            self.hitbox.x -= self.speed


    def fire(self, bullets):
        pass