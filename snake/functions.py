from constants import*
import pygame

def win_lose(snake):


    font = pygame.font.Font(None, 50)
    finish = False
    text = ""

    if scores[0] >= WIN_SCORE:
        finish = True
        text = font.render(WIN_TEXT, True, BLACK)