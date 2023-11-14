from Sprite import Sprite
from Constants import*
import pygame as pg

class Player(Sprite):

    # керування гравцем по клавішам
    def controls(self, left, right, up, down):
        
        # отримання натиснутих в даний момент клавіш
        keys = pg.key.get_pressed()

        # 4 перевірки - 4 клавіші
        # в залежності, яка клавіша була натиснута у нас відбувається рух
        # у відповідну сторону
        if keys[left] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[right] and self.rect.x < WINDOW_WIDTH - 5:
            self.rect.x += self.speed

        if keys[up] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[down] and self.rect.y < WINDOW_HEIGHT - 5:
            self.rect.y += self.speed     

        # нюанси: рух відбувається через зміну координат
        # вгору: -у, вниз: +у, вліво: -х, вправо: +х
        # друга умова після and перевіряє торкання меж, оскільки
        # ми можемо рухатись, поки не вперемось в межу 
