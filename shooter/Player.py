from Sprite import*
from constants import*
from Bullet import*

class Player(Sprite):

    def control(self, left, right):

        key_pressed = pygame.key.get_pressed()
        if key_pressed[left] and self.hitbox.x > 5:
            self.hitbox.x -= self.speed

        if key_pressed[right] and self.hitbox.x < WINDOW_WIDTH - self.hitbox.width - 5:
            self.hitbox.x += self.speed

    def fire(self, bullets):
        bullet = Bullet(BULLET_WIDTH, BULLET_HEIGHT, self.hitbox.centerx, self.hitbox.top, BULLET_IMAGE_PATH, BULLET_SPEED)
        bullets.add(bullet)