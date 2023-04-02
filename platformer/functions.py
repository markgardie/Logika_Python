from constants import*
import pygame

def win_lose(coin, player):

    font = pygame.font.Font(None, 50)
    finish = False
    text = ""

    if player.hitbox.colliderect(coin.hitbox):
        finish = True
        text = font.render(WIN_TEXT, True, BLACK)