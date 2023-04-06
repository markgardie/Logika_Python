from random import randint
from constants import*
import pygame

pygame.init()

def collisions(ball, platform1, platform2):

    if ball.rect.colliderect(platform1.rect):
        direction_x = 1
        direction_y = randint(-1, 1)

    if ball.rect.colliderect(platform2.rect):
        direction_x = -1
        direction_y = randint(-1, 1)

    if ball.rect.y < 5:
        direction_y = 1
    
    if ball.rect.y > WINDOW_HEIGHT - 5:
        direction_y = -1

def win_lose(ball):

    finish = False
    text = ""
    font = pygame.font.Font(None, 50)

    if ball.rect.x < 5:
        finish = True
        text = font.render("Переміг гравець 2", True, BLACK)

    if ball.rect.x > WINDOW_WIDTH - 5:
        finish = True
        text = font.render("Переміг гравець 1", True, BLACK)

    return finish, text
    