import pygame as pg

class Label():

    def __init__(self, x, y, text_size, text_color, text):
        self.font = pg.font.Font(None, text_size)
        self.text = self.font.render(text, True, text_color)

        self.x = x
        self.y = y
        self.text_color = text_color

    def change_text(self, text):
        self.text = self.font.render(text, True, self.text_color)
