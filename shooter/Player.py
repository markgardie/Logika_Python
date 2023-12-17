from Sprite import*
from Constants import*
from Bullet import*

class Player(Sprite):

    def controls(self, left, right):

        keys = pygame.key.get_pressed()

        if keys[right] and self.rect.x < WINDOW_WIDTH - 10:
            self.rect.x += self.speed

    def fire(self, bullets):
        bullet = Bullet(BULLET_WIDTH, BULLET_HEIGHT, 
                        self.rect.centerx, self.rect.top, 
                        BULLET_IMAGE_PATH, BULLET_SPEED)
        bullets.add(bullet)
        
        
