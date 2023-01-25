from classes.Sprite import*
from constants import*

class Enemy(Sprite):

    def move(self):

        

        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= WINDOW_WIDTH - 85:
            self.direction = "left"


        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
