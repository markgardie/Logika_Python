import pygame as pg

class Window():

    def __init__(self, width, height, bg_image_path, caption):
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(caption)

        self.image = pg.image.load(bg_image_path)
        self.image = pg.transform.scale(self.image, (width, height))

        self.screen.blit(self.image, (0, 0))

        self.clock = pg.time.Clock()
