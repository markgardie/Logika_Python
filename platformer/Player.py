from Sprite import*

class Player(Sprite):

    def controls(self, up, left, right):

        key_pressed = pygame.key.get_pressed()

        if key_pressed[left] and self.hitbox.x > 5:
            self.hitbox.x -= self.speed

        if key_pressed[right] and self.hitbox.x < WINDOW_WIDTH - 5:
            self.hitbox.x += self.speed


    def gravity(self, platforms):

        down = True

        for platform in platforms:
            if self.hitbox.colliderect(platform.hitbox):
                down = False

        if down:
            self.hitbox.y += self.speed
