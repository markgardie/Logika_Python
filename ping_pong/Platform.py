from Sprite import*
from constants import*

class Platform(Sprite):

    def controls(self, up, down):
        
        key_pressed = pygame.key.get_pressed()

        if key_pressed[up] and self.rect.y > 5:
            self.rect.y -= self.speed

        if key_pressed[down] and self.rect.y < WINDOW_HEIGHT - 5:
            self.rect.y += self.speed