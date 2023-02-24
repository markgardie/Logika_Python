from Sprite import*
from constants import*

class Player(Sprite):

    def control(self, left, right):

        key_pressed = pg.key.get_pressed()
        if key_pressed[left] and self.rect.x > 5:
            self.rect.x -= self.speed

        if key_pressed[right] and self.rect.x < WINDOW_WIDTH - self.rect.width - 5:
            self.rect.x += self.speed