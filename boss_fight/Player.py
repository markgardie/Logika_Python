from Sprite import*
from constants import*

class Player(Sprite):

    def controls(self, left, right, up, down):

        key_pressed = pygame.key.get_pressed()

        if key_pressed[left] and self.hitbox.x > 5:
            self.hitbox.x -= self.speed

        if key_pressed[right] and self.hitbox.x < WINDOW_WIDTH - 5:
            self.hitbox.x += self.speed

        if key_pressed[up] and self.hitbox.y > 5:
            self.hitbox.y -= self.speed

        if key_pressed[down] and self.hitbox.y < WINDOW_HEIGHT- 5:
            self.hitbox.y += self.speed