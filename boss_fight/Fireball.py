from Sprite import*
from random import randint

# спадкується від базового класу Спрайт
# копіює хітбокс та зображення
class Fireball(Sprite):

    # конструктор
    # властивості фаєрбола: розміри, координати, шлях до картинки, швидкість (копіюються зі Спрайта)
    # нові властивості: напрямки
    def __init__(self, width, height, x, y, image_path, speed, dir_x, dir_y):

        # викликаємо конструктор у супер-класу (у Спрайта)
        super().__init__(width, height, x, y, image_path, speed)

        # додаємо нові властивості: напрямки
        self.dir_x = dir_x
        self.dir_y = dir_y

    # рух фаєрболп а певному напрямку
    def move(self):
       
        # зміна координат
        # рух з певною швидкістю (speed)
        # в певних напрямках
        self.hitbox.x += self.speed * self.dir_x
        self.hitbox.y += self.speed * self.dir_y