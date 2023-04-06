from Sprite import*

class Bullet(Sprite):

    def move(self, direction_x):
        self.hitbox.x += self.speed * direction_x