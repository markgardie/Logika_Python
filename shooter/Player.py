from Sprite import Sprite
from Bullet import Bullet
from Constants import*

class Player(Sprite):

    def controls(self, left, right, up, down):
        
        keys = pg.key.get_pressed()

        if keys[left] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[right] and self.rect.x < WINDOW_WIDTH - 5:
            self.rect.x += self.speed

        if keys[up] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[down] and self.rect.y < WINDOW_HEIGHT - 5:
            self.rect.y += self.speed      

    def fire(self, bullets):
        bullet = Bullet(
            BULLET_WIDTH, BULLET_HEIGHT,
            self.rect.centerx, self.rect.top,
            BULLET_IMAGE_PATH, BULLET_SPEED
        )
        bullets.add(bullet)