from Sprite import Sprite
from Constants import*

class Enemy(Sprite):

    def move(self):

        if self.rect.x <= MONSTER_RIGHT_POINT:
            self.direction = "right"
        if self.rect.x >= MONSTER_LEFT_POINT:
            self.direction = "left"


        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed