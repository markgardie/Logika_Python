
from Sprite import*

class Bullet(Sprite):

    def move(self):

        self.hitbox.y -= self.speed

        if self.hitbox.y < 0:
            self.kill()

    def update(self):
        self.move()

