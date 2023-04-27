from Sprite import*
from constants import*

class Player(Sprite):

    def controls(self, up, left, right, platforms):

        key_pressed = pygame.key.get_pressed()

        if key_pressed[left] and self.hitbox.x > 5:
            self.hitbox.x -= self.speed

        if key_pressed[right] and self.hitbox.x < WINDOW_WIDTH - 5:
            self.hitbox.x += self.speed

        for platform in platforms:
            if key_pressed[up] and self.hitbox.y > 5 and self.hitbox.colliderect(platform.hitbox):
                self.hitbox.y -= self.speed * 20


    def gravity(self, platforms):

        down = True

        for platform in platforms:
            if self.hitbox.colliderect(platform.hitbox):
                down = False

        if down:
            self.hitbox.y += self.speed
