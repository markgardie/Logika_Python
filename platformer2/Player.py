from Sprite import*
from constants import*


# клас Гравець спадкується від базового класу Спрайт
# копіює хітбокс та зображення
# доповнює керуванням та гравітацією
class Player(Sprite):

    # керування
    # в параметрах: 3 різних кнопки та напрямку
    # також в параметрах платформи, оскільки стрибок залежиться
    # від торкання платформи
    def controls(self, up, left, right, platforms):

       # отримуємо натиснуті кнопки
        keys = pygame.key.get_pressed()

        # циклом проходимось по всім платформам
        for platform in platforms:
            # якщо натиснуто на клавішу вгору
            # і не досягнули верхньої межі (0)
            # і гравець торкається платформи 
            if keys[up] and self.hitbox.y > 0 and self.hitbox.colliderect(platform.hitbox):
                # робимо стрибок
                # множення на 100 треба, аби перебороти гравітацію
                # стрибок - це рух вгору
                # рух вгору - це -у
                self.hitbox.y -= self.speed * 20
                
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
