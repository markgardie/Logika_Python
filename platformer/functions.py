import pygame
from constants import*

pygame.init()

def win_lose(player, coin):

    font = pygame.font.Font(None, 50)

    finish = False
    text = ""

    if player.hitbox.colliderect(coin.hitbox):
        finish = True
        text = font.render("Ти переміг", True, BLACK)

    if player.hitbox.y >= WINDOW_HEIGHT - 10:
        finish = True
        text = font.render("Ти програв", True, BLACK)

    return finish, text