import pygame

# запускає (ініціалізує) pygame
# потрібно для шрифтів та текстів
pygame.init()

# базовий клас
# ми його використовуємо і копіюємо в багатьох проектах
class Sprite():
    
    # конструктор
    # викликається при створенні об'єкта
    # характеристики: розміри, координати, шлях до картинки, швидкість
    def __init__(self, width, height, x, y, image_path, speed):

        # створює хітбокс (прямокутник)
        self.hitbox = pygame.Rect(x, y, width, height)

        # завантажує картинку по шляху
        self.image = pygame.image.load(image_path)
        # змінює розмір
        # розмір картинки і хітбокса повинні бути однакові
        self.image = pygame.transform.scale(self.image, (width, height))

        # записуємо швидкість
        self.speed = speed