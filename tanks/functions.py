import pygame
from constants import*

pygame.init()

def win_lose(player1, player2, bullets):

    font = pygame.font.Font(None, 50)

    for bullet in bullets:
        if player1.hitbox.colliderect(bullet.hitbox):
            finish = True
            text = font.render("Переміг гравець 2", True, BLACK)

        if player2.hitbox.colliderect(bullet.hitbox):
            finish = True
            text = font.render("Переміг гравець 1", True, BLACK)


    if player1.hitbox.colliderect(player2.hitbox):
            finish = True
            text = font.render("Нічия", True, BLACK)


