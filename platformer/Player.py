from Sprite import*
from constants import*

class Player(Sprite):

    def controls(self, left, right, up):
        keys = pygame.key.get_pressed()

        if keys[up] and self.hitbox.y > 0:
            self.hitbox.y -= self.speed

        if keys[left] and self.hitbox.x > 0:
            self.hitbox.x -= self.speed

        if keys[right] and self.hitbox.x < WINDOW_WIDTH:
            self.hitbox.x += self.speed

    def gravity(self, platforms):
        
        down = True

        for platform in platforms:

            if self.hitbox.colliderect(platform.hitbox):
                down = False

        if down:
            self.hitbox.y += GRAVITY_SPEED