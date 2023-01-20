from classes.Sprite import*
from constants import*

class Enemy(Sprite):

    def move(self):

        

        if self.hitbox.x <= 470:
            self.direction = "right"
        if self.hitbox.x >= WINDOW_WIDTH - 85:
            self.direction = "left"


        if self.direction == "left":
            self.hitbox.x -= self.speed
        else:
            self.hitbox.x += self.speed
