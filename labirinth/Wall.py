import pygame as pg

pg.init()

class Wall(pg.sprite.Sprite):

    # конструктор
    # потрібен для початкових налаштувань та властивостей 
    def __init__(self, color1, color2, color3, x, y, width, heigth):
        super().__init__()

        # створення пустого зображення (полотна)
        # для подальшої заливки
        self.image = pg.Surface((width, heigth))
        self.image.fill((color1, color2, color3))

        # створення та налаштування хітбоксу
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # нюанси: розповісти про схему RGB