import pygame as pg

# базовий клас спрайт
# підходить для багатьох ігор
# спадкується від встроєного в pygame класу Sprite
class Sprite(pg.sprite.Sprite):

    # конструктор
    # властивості: розміри, координати, шлях до зображення, швидкість спрайту
    def __init__(self, width, height, x, y, image_path, speed):
        # запускаємо конструктор класу із pygame
        pg.sprite.Sprite.__init__(self)

        # використовуємо відразу дві функції
        # load - для завантаження зображення
        # scale - для зміни розмірів зображення під хітбокс
        self.image = pg.transform.scale(pg.image.load(image_path), (width, height))

        # хітбокс створюємо отримавши прямокутник зображення
        self.rect = self.image.get_rect()

        # задаємо координати хітбокус
        self.rect.x = x
        self.rect.y = y

        # задаємо швидкість
        self.speed = speed
