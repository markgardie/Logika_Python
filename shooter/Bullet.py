from HitboxSprite import*
from Constants import*

class Bullet(HitboxSprite):

    def move(self):
        self.rect.y -= self.speed

        if self.rect.y < 0:
            self.kill()

    def update(self):
        self.move()