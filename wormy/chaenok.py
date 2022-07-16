import pygame
from constants import*
pygame.init()

def draw_worm(worm_coords, window):
    for coord in worm_coords:
        x = coord["x"] * CELL_SIZE
        y = coord["y"] * CELL_SIZE
        worm_rect = pygame.Rect(x , y , CELL_SIZE , CELL_SIZE)
        pygame.draw.rect(window, DARK_GREEN , worm_rect)
        cell_rect = pygame.Rect(x + 4 , y + 4 , CELL_SIZE - 8 , CELL_SIZE - 8)
        pygame.draw.rect(window, GREEN , cell_rect)