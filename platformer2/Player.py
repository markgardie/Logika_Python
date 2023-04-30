from Sprite import*
from constants import*

class Player(Sprite):

    def controls(self, up, left, right, platforms):

        key_pressed = pygame.key.get_pressed()

        if key_pressed[left] and self.hitbox.x > 5:
            self.hitbox.x -= self.speed

        if key_pressed[right] and self.hitbox.x < WINDOW_WIDTH - 5:
            self.hitbox.x += self.speed

        for platform in platforms:
            if key_pressed[up] and self.hitbox.y > 5 and self.hitbox.colliderect(platform.hitbox):
                self.hitbox.y -= self.speed * 20

    # запускає гравітацію
    # platforms треба для перевірки колізій із платформами
    # гравітація залежить від платформ
    def gravity(self, platforms):

        # відповідає за увімкнення гравітації
        # True - гравітаціє є
        # False - гравітації немає
        down = True

        # перебирає всі платформи в списку
        for platform in platforms:
            # перевірка торкання гравця і платформи
            if self.hitbox.colliderect(platform.hitbox):
                # якщо торкається, то
                # гравітації немає
                down = False

        # якщо гравітаціє є, то
        if down:
            # падаємо вниз з певною швидкістю (speed)
            self.hitbox.y += self.speed
