import pygame as pg

class Sprite(pg.sprite.Sprite):

    # конструктор
    # потрібен для початкових налаштувань та властивостей 
    def __init__(self, width, height, x, y, image_path, speed):

        pg.sprite.Sprite.__init__(self)

        # створення хітбокса
        self.rect = pg.Rect(x, y, width, height)

        # робота із зображеннями
        self.image = pg.image.load(image_path)
        self.image = pg.transform.scale(self.image, (width, height))
        
        # швидкість
        self.speed = speed

        # Нюанси: наш клас Sprite спадкується від пайгеймовського класу Sprite
        # Це треба для можливість додавання цього спрайта в групу