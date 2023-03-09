from Sprite import*

class Bullet(Sprite):

    def move(self):

        self.rect.y -= self.speed

        if self.rect.y < 0:
            self.kill()

    def update(self):
        self.move()
        