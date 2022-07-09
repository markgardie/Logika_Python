import pygame
from constants import*

def show_start_screen(window):
    font = pygame.font.Font("freesansbold.ttf", 100)

    text1 = font.render("Wormy!", True, WHITE, DARKGREEN)
    text2 = font.render("Wormy!", True, GREEN)

    while True:
        window.fill(BG_COLOR)