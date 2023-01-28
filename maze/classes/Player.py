from classes.Sprite import*
from constants import*
class Player(Sprite):

    def control(self, left, right, up, down):

        self.key_pressed = pygame.key.get_pressed()

        if  self.key_pressed[left] and self.rect.x > 5:
            self.rect.x -= self.speed
        if self.key_pressed[right] and self.rect.x < WINDOW_WIDTH - 80:
            self.rect.x += self.speed
        if self.key_pressed[up] and self.rect.y > 5:
            self.rect.y -= self.speed
        if self.key_pressed[down] and self.rect.y < WINDOW_HEIGHT - 80:
            self.rect.y += self.speed