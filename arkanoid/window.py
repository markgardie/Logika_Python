import pygame as pg

class Window():

    def __init__(self, width, height, caption, bg_color):
        
        size = (width, height)

        self.background = pg.display.set_mode(size)
        pg.display.set_caption(caption)

        self.background.fill(bg_color)

        self.clock = pg.time.Clock()