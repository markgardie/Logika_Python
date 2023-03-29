import pygame
from constants import*

pygame.init()

def draw_bullets(window, bullets1, bullets2):
     
    for bullet in bullets1:
        window.blit(bullet.image, (bullet.hitbox.x, bullet.hitbox.y))
    
    for bullet in bullets2:
        window.blit(bullet.image, (bullet.hitbox.x, bullet.hitbox.y))


def move_bullets(bullets1, bullets2):
     
    for bullet in bullets1:
        bullet.move(1)
    
    for bullet in bullets2:
        bullet.move(-1)

def win_lose(player1, player2, bullets1, bullets2):

    finish = False
    text = ""

    font = pygame.font.Font(None, 50)

    for bullet in bullets1:
        if player2.hitbox.colliderect(bullet.hitbox):
            finish = True
            text = font.render("Переміг гравець 1", True, BLACK)

    
    for bullet in bullets2:

        if player1.hitbox.colliderect(bullet.hitbox):
            finish = True
            text = font.render("Переміг гравець 2", True, BLACK)


    if player1.hitbox.colliderect(player2.hitbox):
            finish = True
            text = font.render("Нічия", True, BLACK)

    return finish, text


