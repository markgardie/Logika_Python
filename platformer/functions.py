from constants import*
import pygame

scores = 0

def win_lose(player, enemy):

    global scores

    font = pygame.font.Font(None, 50)
    finish = False
    text = ""

    if scores == 3:
        finish = True
        text = font.render(WIN_TEXT, True, BLACK)

    if player.hitbox.colliderect(enemy.hitbox):
        finish = True
        text = font.render(LOSE_TEXT, True, BLACK)

    return finish, text

def collisions(player, coins):

    global scores

    for coin in coins:
        if player.hitbox.colliderect(coin.hitbox):
            scores += 1