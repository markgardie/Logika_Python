from classes.Sprite import *
from constants import*

class Player(Sprite):

    def control(self, left, right, up, down):

        self.key_pressed = pygame.key.get_pressed()

        if  self.key_pressed[left] and self.hitbox.x > 5:
            self.hitbox.x -= self.speed
        if self.key_pressed[right] and self.hitbox.x < WINDOW_WIDTH - 80:
            self.hitbox.x += self.speed
        if self.key_pressed[up] and self.hitbox.y > 5:
            self.hitbox.y -= self.speed
        if self.key_pressed[down] and self.hitbox.y < WINDOW_HEIGHT - 80:
            self.hitbox.y += self.speed