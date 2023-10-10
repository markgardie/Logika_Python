import pygame as pg

class Window():
    
    def __init__(self, width, heigth, caption, bg_color):

        size = (width, heigth)

        # створення екрана 
        self.screen = pg.display.set_mode(size)
        # виставлення надпису, заголовку екрана
        pg.display.set_caption(caption)

        # заливка фону певним кольором
        self.screen.fill(bg_color)

        # створення годинника для тіків
        self.clock = pg.time.Clock()