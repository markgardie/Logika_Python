from Sprite import*
from Constants import*
from Bullet import*

class Tank(Sprite):

    def controls(self, left, right, up, down):

        # отримуємо список клавіш, які були натиснуті
        keys = pg.key.get_pressed()

        # натискання клавіші вгору і не торкання верхньої межі
        if keys[up] and self.hitbox.y > 0:
            self.hitbox.y -= self.speed

        # натискання клавіші вниз і не торкання нижньох межі
        if keys[down] and self.hitbox.y < WINDOW_HEIGHT:
            self.hitbox.y += self.speed

        # натискання клавіші вліво і не торкання лівої межі
        if keys[left] and self.hitbox.x > 0:
            self.hitbox.x -= self.speed

        # натискання клавіші вправо і не торкання правої межі
        if keys[right] and self.hitbox.x < WINDOW_WIDTH:
            self.hitbox.x += self.speed

    # постріл першого танку
    def fire1(self, bullets1):
        # створення нової кулі
        # яка заходиться справа, по центру від хітбокса першого танку
        bullet = Bullet(BULLET_WIDTH, BULLET_HEIGHT, self.hitbox.right, self.hitbox.centery, BULLET_IMAGE_PATH, BULLET_SPEED)
        # додавання кулі в список куль
        bullets1.append(bullet)

    # постріл другого танку
    def fire2(self, bullets2):
        # створення нової кулі
        # яка заходиться зліва, по центру від хітбокса другого танку
        bullet = Bullet(BULLET_WIDTH, BULLET_HEIGHT, self.hitbox.left, self.hitbox.centery, BULLET_IMAGE_PATH, BULLET_SPEED)
        # додавання кулі в список куль
        bullets2.append(bullet)