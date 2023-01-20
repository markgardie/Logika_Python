import pygame

pygame.init()

class Card():

    def __init__(self, x, y, width, height, color, text, text_size, text_color, font):
        self.hitbox = pygame.Rect(x, y, width, height)

        self.color = color

        self.text = pygame.font.SysFont(font, text_size).render(text, True, text_color)

    def set_color(self, new_color):
        self.color = new_color

    def collide(self, x, y):
        return self.hitbox.collidepoint(x, y)
    