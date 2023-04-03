from Sprite import*
from constants import*
import time

# клас Гравець спадкується від базового класу Спрайт
# копіює хітбокс та зображення
# доповнює керуванням та гравітацією
class Player(Sprite):
    
    # керування
    # в параметрах: 3 різних кнопки та напрямку
    # також в параметрах платформи, оскільки стрибок залежиться
    # від торкання платформи
    def controls(self, left, right, up, platforms):

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
                self.hitbox.y -= self.speed * 100
                
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

    # гравітація
    # в параметрах отримуємо платформи
    # оскільки наявність гравітації залежить від 
    # торкання з платформами
    def gravity(self, platforms):
        
        # змінна, яка показує, чи є гравітація
        # на початку запускаємо гравітацію
        down = True

        # циклом перебираємо всі платформи
        for platform in platforms:
            
            # якщо гравець торкається платформи
            if self.hitbox.colliderect(platform.hitbox):
                # гравітація пропадає
                down = False

        # якщо є гравітація
        if down:
            # рухаємось вниз
            # рух вниз це +у
            self.hitbox.y += GRAVITY_SPEED