from Sprite import*
from constants import*

class Player(Sprite):

    def control(self, left, right):

        key_pressed = pygame.key.get_pressed()
        if key_pressed[left] and self.hitbox.x > 5:
            self.hitbox.x -= self.speed

        if key_pressed[right] and self.hitbox.x < WINDOW_WIDTH - self.hitbox.width - 5:
            self.hitbox.x += self.speed