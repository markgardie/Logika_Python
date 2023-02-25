from Sprite import*

class Platform(Sprite):

    def controls(self, left, right):

        keys = pygame.key.get_pressed()

        if keys[left] and self.hitbox.x > 5:
            self.hitbox.x -= self.speed
        if keys[right] and self.hitbox.x < WINDOW_WIDTH - 5:
            self.hitbox.x += self.speed