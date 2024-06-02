import pygame as pg

class Window():
    
    def __init__(self, width, heigth, caption, bg_path):

        size = (width, heigth)

        self.screen = pg.display.set_mode(size)
        pg.display.set_caption(caption)

        self.bg_image = pg.image.load(bg_path)
        self.bg_image = pg.transform.scale(self.bg_image, size)

        self.clock = pg.time.Clock()

    def draw(self):
        self.screen.blit(self.bg_image, (0, 0))