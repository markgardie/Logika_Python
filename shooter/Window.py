import pygame as pg

class Window():
    
    def __init__(self, width, heigth, caption, bg_image_path):

        size = (width, heigth)

        self.screen = pg.display.set_mode(size)
        pg.display.set_caption(caption)

        self.image = pg.image.load(bg_image_path)
        self.image = pg.transform.scale(self.image, size)

        self.clock = pg.time.Clock()