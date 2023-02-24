import pygame as pg

pg.init()

class Window():

    def __init__(self, width, height, caption, background):

        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(caption)

        self.bg_image = pg.image.load(background)
        self.bg_image = pg.transform.scale(self.bg_image, (width, height))

        self.clock = pg.time.Clock()
    