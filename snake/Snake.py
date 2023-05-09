from Sprite import*


# спадкується від Спрайту
# копіює хітбокс та зображення
class Snake(Sprite):

    # конструктор
    # запускається при створенні об'єкту
    # властивості: розміри, координати, колір, швидкість
    def __init__(self, width, height, x, y, color, speed):
        # запускаємо конструктор супер-класу (батьківського класу Спрайт)
        # таким чином копіюємо код Спрайта
        super().__init__(width, height, x, y, color, speed)

        # додаємо нові властивості, які треба тільки змійці
        # напрямки руху
        self.direction_x = 1
        self.direction_y = 0

    # метод керування
    # в параметрах отримуємо напрямки
    def controls(self, up, down, left, right):
        
        # отримуємо, які клавіші були натиснуті в даний момент
        key_pressed = pygame.key.get_pressed()

        # якщо натиснута клавіша вліво
        if key_pressed[left]:
            self.direction_x = -1
            self.direction_y = 0
        # якщо натиснута клавіша вправо
        if key_pressed[right]:
            self.direction_x = 1
            self.direction_y = 0
        # якщо натиснута клавіша вгору
        if key_pressed[up]:
            self.direction_x = 0
            self.direction_y = -1
        # якщо натиснута клавіша вниз
        if key_pressed[down]:
            self.direction_x = 0
            self.direction_y = 1
    
    # автоматичний рух змійки
    def move(self):
        # рух з певною швидкістю та напрямком
        self.hitbox.x += self.speed * self.direction_x
        self.hitbox.y += self.speed * self.direction_y