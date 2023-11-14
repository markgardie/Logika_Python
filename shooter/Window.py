import pygame as pg

class Window():
    
    # конструктор
    # потрібен для початкових налаштувань та властивостей 
    def __init__(self, width, heigth, caption, bg_image_path):

        # створення та налаштування вікна, розмірів
        size = (width, heigth)
        self.screen = pg.display.set_mode(size)
        pg.display.set_caption(caption)

        # робота із зображенням для фону
        self.image = pg.image.load(bg_image_path)
        self.image = pg.transform.scale(self.image, size)

        # годинник
        self.clock = pg.time.Clock()

        # Нюанси: функція scale треба для зміни розмірів завантаженого зображення
        # під розміри вікна