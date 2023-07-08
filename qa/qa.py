import pygame as pg

# запускається модуль зі шрифтами
pg.font.init()


class Window():
    
    def __init__(self, width, heigth, caption, bg_color):

        size = (width, heigth)

        self.screen = pg.display.set_mode(size)
        pg.display.set_caption(caption)

        self.screen.fill(bg_color)

class Button():

    def __init__(self, 
                 width, height, 
                 x, y, color, 
                 text, text_size, font, text_color):
        
        self.rect = pg.Rect(x, y, width, height)
        self.color = color

        self.font = pg.font.Font(font, text_size)
        self.text = self.font.render(text, True, text_color)

