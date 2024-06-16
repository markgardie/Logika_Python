from shooter.HitboxSprite import*
from Constants import*
from Bullet import*

class Player(HitboxSprite):

    
    def controls(self, left, right):
        keys = pg.key.get_pressed()

        if keys[right] and self.rect.x < WINDOW_WIDTH:
            self.rect.x += self.speed

        if keys[left] and self.rect.x > 0:
            self.rect.x -= self.speed


    def fire(self, bullets):
        bullet = Bullet(BULLET_WIDTH, BULLET_HEIGHT, 
                        self.rect.centerx, self.rect.top, 
                        BULLET_IMAGE_PATH, BULLET_SPEED)
        bullets.add(bullet)
        