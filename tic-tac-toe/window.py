import pygame as pg

class Window():

    def __init__(self, width, height, bg_color, caption):
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(caption)

        self.screen.fill(bg_color)

        self.clock = pg.time.Clock()
