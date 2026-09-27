import pygame
from constants import*

class Button:

    def __init__(self, 
                 coords, 
                 size, 
                 bg_color, 
                 text_color, 
                 font_family, 
                 text_size,
                 text):
        self.rect = pygame.Rect(coords[0], coords[1], size[0], size[1])
        self.bg_color = bg_color
        self.font = pygame.font.Font(font_family, text_size)
        self.text = self.font.render(text, True, text_color)

    def update(self, fun, event):
        if (event.type == pygame.MOUSEBUTTONDOWN
            and event.key == 1
            and self.rect.collidepoint(event.pos)
            ):
            fun()

    def draw(self, surface):
        text_x = self.rect.width / 2 - self.text.get_width() / 2
        text_y = self.rect.height / 2 - self.text.get_height() / 2
        pygame.draw.rect(surface, self.bg_color, self.rect)
        surface.blit(self.text, (text_x, text_y))
