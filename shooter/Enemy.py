from HitboxSprite import*
from Constants import*

class Enemy(HitboxSprite):

    def move(self):
        self.rect.y += self.speed

        if self.rect.y > WINDOW_HEIGHT:
            self.kill()

    def update(self):
        self.move()