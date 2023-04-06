from Sprite import*
from constants import*
from Bullet import*

class Tank(Sprite):

    def controls(self, left, right, up, down):

        keys = pygame.key.get_pressed()

        if keys[up] and self.hitbox.y > 0:
            self.hitbox.y -= self.speed

        if keys[down] and self.hitbox.y < WINDOW_HEIGHT:
            self.hitbox.y += self.speed

        if keys[left] and self.hitbox.x > 0:
            self.hitbox.x -= self.speed

        if keys[right] and self.hitbox.x < WINDOW_WIDTH:
            self.hitbox.x += self.speed

    def fire1(self, bullets1):
        bullet = Bullet(BULLET_WIDTH, BULLET_HEIGHT, self.hitbox.right, self.hitbox.centery, BULLET_IMAGE_PATH, BULLET_SPEED)
        bullets1.append(bullet)

    def fire2(self, bullets2):
        bullet = Bullet(BULLET_WIDTH, BULLET_HEIGHT, self.hitbox.left, self.hitbox.centery, BULLET_IMAGE_PATH, BULLET_SPEED)
        bullets2.append(bullet)