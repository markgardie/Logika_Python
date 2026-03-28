import pygame

pygame.init()

class Card():

    def __init__(self, x, y, width, height, color, text, text_size, text_color, font):
        
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

        self.font = pygame.font.Font(font, text_size)
        self.text = self.font.render(text, True, text_color)
    
    def set_color(self, color):
        self.color = color