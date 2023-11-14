from Sprite import Sprite
from Bullet import Bullet
from Constants import*

class Player(Sprite):

    # керування гравцем по клавішам
    def controls(self, left, right, up, down):
        
        # отримання натиснутих в даний момент клавіш
        keys = pg.key.get_pressed()

        # 4 перевірки - 4 клавіші
        # в залежності, яка клавіша була натиснута у нас відбувається рух
        # у відповідну сторону
        if keys[left] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[right] and self.rect.x < WINDOW_WIDTH - 5:
            self.rect.x += self.speed

        if keys[up] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[down] and self.rect.y < WINDOW_HEIGHT - 5:
            self.rect.y += self.speed     

        # нюанси: рух відбувається через зміну координат
        # вгору: -у, вниз: +у, вліво: -х, вправо: +х
        # друга умова після and перевіряє торкання меж, оскільки
        # ми можемо рухатись, поки не вперемось в межу 

    # постріл
    def fire(self, bullets):
        
        # створюється нова куля
        bullet = Bullet(
            BULLET_WIDTH, BULLET_HEIGHT,
            # вона з'являється зверху по центру від нашого персонажа
            self.rect.centerx, self.rect.top,
            BULLET_IMAGE_PATH, BULLET_SPEED
        )

        # додаємо кулю в групу куль
        bullets.add(bullet)