from Sprite import*
from constants import*
from Bullet import*

# Танк спадкується від базового класу Спрайт
# копіює хітбокс та зображення
# доповнює керуванням та вистрілом
class Tank(Sprite):

    # керування
    # в параметрах: 4 різних кнопки та напрямку
    def controls(self, left, right, up, down):

        # отримуємо натиснуті кнопки
        keys = pygame.key.get_pressed()

        # якщо натиснуто на клавішу вгору
        # і при цьому не вийшли за верхню межу (0)
        if keys[up] and self.hitbox.y > 0:
            # рухаємо персонажа вгору
            # рух вгору це -у
            self.hitbox.y -= self.speed

        # якщо натиснуто на клавішу вниз
        # і при цьому не вийшли за нижню межу (висота вікна)
        if keys[down] and self.hitbox.y < WINDOW_HEIGHT:
            # рухаємо персонажа вниз
            # рух вниз це +у
            self.hitbox.y += self.speed

        # якщо натиснуто на клавішу вліво
        # і при цьому не вийшли за ліву межу (0)
        if keys[left] and self.hitbox.x > 0:
            # рухаємо персонажа вліво
            # рух вліво це -х
            self.hitbox.x -= self.speed

        # якщо натиснуто на клавішу вправо
        # і при цьому не вийшли за праву межу (ширина вікна)
        if keys[right] and self.hitbox.x < WINDOW_WIDTH:
            # рухаємо персонажа вправо
            # рух вправо це +х
            self.hitbox.x += self.speed

    # вистріл першого танку
    def fire1(self, bullets1):
        # снаряд з'являється справа
        # параметр self.hitbox.right
        bullet = Bullet(BULLET_WIDTH, BULLET_HEIGHT, self.hitbox.right, self.hitbox.centery, BULLET_IMAGE_PATH, BULLET_SPEED)
        # додаємо снаряд в список снарядів
        bullets1.append(bullet)

    # вистріл другого танку
    def fire2(self, bullets2):
        # снаряд з'являється злів
        # параметр self.hitbox.left
        bullet = Bullet(BULLET_WIDTH, BULLET_HEIGHT, self.hitbox.left, self.hitbox.centery, BULLET_IMAGE_PATH, BULLET_SPEED)
        # додаємо снаряд в список снарядів
        bullets2.append(bullet)