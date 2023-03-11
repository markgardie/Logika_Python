from Sprite import*
from constants import*
from Bullet import*

class Player(Sprite):

    def control(self, left, right):

        key_pressed = pygame.key.get_pressed()
        if key_pressed[left] and self.rect.x > 5:
            self.rect.x -= self.speed

        if key_pressed[right] and self.rect.x < WINDOW_WIDTH - self.rect.width - 5:
            self.rect.x += self.speed

    def fire(self, bullets):
        bullet = Bullet(BULLET_WIDTH, BULLET_HEIGHT, self.rect.centerx, self.rect.top, BULLET_IMAGE_PATH, BULLET_SPEED)
        bullets.add(bullet)