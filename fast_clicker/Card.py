import pygame
from constants import*

pygame.init()

class Card():

    def __init__(self, x, y, color, width, height):

        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

        self.font = pygame.font.Font(FONT, TEXT_SIZE)
        self.text = self.font.render(TEXT, True, TEXT_COLOR)