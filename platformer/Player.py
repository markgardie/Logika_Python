from Sprite import*

class Player(Sprite):

    def controls(self, left, right, up):
        keys = pygame.key.get_pressed()

        if keys[up] and self.hitbox.y > 0:
            self.hitbox.y -= self.speed
