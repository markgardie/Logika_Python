import pygame as pg

class Window():
    
    def __init__(self, width, heigth, caption, bg_color):

        size = (width, heigth)

        self.screen = pg.display.set_mode(size)
        pg.display.set_caption(caption)

        self.screen.fill(bg_color)

        self.clock = pg.time.Clock()