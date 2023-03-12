from Sprite import*
from constants import*

class Platform(Sprite):
    
    
    def controls(self, left, right):

        keys = pygame.key.get_pressed()

        if keys[left] and self.hitbox.x > 0:
            self.hitbox.x -= PLATFORM_SPEED

        if keys[right] and self.hitbox.x < WINDOW_WIDTH:
            self.hitbox.x += PLATFORM_SPEED

