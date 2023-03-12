from Sprite import*
from constants import*

class Platform(Sprite):

    def controls(self, left, right):

        key_pressed = pygame.key.get_pressed()

        if key_pressed[left] and self.hitbox.x > 5:
            self.hitbox.x -= PLATFORM_SPEED

        if key_pressed[right] and self.hitbox.x < WINDOW_WIDTH - 5:
            self.hitbox.x += PLATFORM_SPEED