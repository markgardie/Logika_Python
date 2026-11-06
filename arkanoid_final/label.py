import pygame as pg


class Label():

    def __init__(self, font_family, text_size, text_color, text):
        self.font = pg.font.Font(font_family, text_size)
        self.text_image = self.font.render(
            text,
            True,
            text_color
        )

    # Відображення тексту
    def draw(self, x, y, surface):
        surface.blit(self.text_image, (x, y))