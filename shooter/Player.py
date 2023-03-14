from Sprite import*
from constants import*
from Bullet import*

# гравець є спрайтом, тому спадкується від нього
class Player(Sprite):

    # метод керування
    def control(self, left, right):
        
        # отримуємо список натиснутих клавіш
        key_pressed = pg.key.get_pressed()

        # якщо була натиснута ліва клавіша
        # і при цьому гравець не вийшов за ліву межу
        # ліва межа - це 0, проте ми пишемо 5 для невеличкого відступу
        if key_pressed[left] and self.rect.x > 5:
            # рухаємо гравця вліво (-х) на певну швидкість
            self.rect.x -= self.speed

        # якщо була натиснута права клавіша
        # і при цьому гравець не вийшов за праву межу
        # ліва межа - це ширина вікна, проте ми пишемо 5 для невеличкого відступу
        if key_pressed[right] and self.rect.x < WINDOW_WIDTH - self.rect.width - 5:
            # рухаємо гравця вліво (+х) на певну швидкість
            self.rect.x += self.speed

    # постріл
    # в параметрах запитуємо групу куль, аби в неї додати нову
    def fire(self, bullets):

        # створюємо нову кулю
        # вона повинна з'явитись посередині ракети, вгору на носі
        # centerx (центр)
        # top (вершина)
        bullet = Bullet(BULLET_WIDTH, BULLET_HEIGHT, self.rect.centerx, self.rect.top, BULLET_IMAGE_PATH, BULLET_SPEED)
        # додаємо кулю в групу куль
        bullets.add(bullet)