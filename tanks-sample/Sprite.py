import pygame as pg

# основний клас
class Sprite():

    
    def __init__(self, width, height, x, y, image_path, speed):

        # хітбокс - головна частина спрайта
        # відповідає за переміщення, колізії 
        self.hitbox = pg.Rect(x, y, width, height)

        # картинка для оформлення
        # завантажуємо по шляху
        self.image = pg.image.load(image_path)
        # змінюємо розміри, аби були однакові із хітбоксом
        self.image = pg.transform.scale(self.image, (width, height))

        self.speed = speed