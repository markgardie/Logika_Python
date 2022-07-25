import pygame
from constants import*

def make_text(text, text_color, bg_color, top, left):
    font = pygame.font.Font("freesansbold.ttf", FONT_SIZE)
    final_text = font.render(text, True, text_color, bg_color)
    final_text_rect = final_text.get_rect()
    final_text_rect.topLeft = (top, left)
    return text, text.rect