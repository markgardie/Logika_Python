from constants import*
import pygame

def win_lose(player, enemy, scores):

    font = pygame.font.Font(None, 50)
    finish = False
    text = ""

    if scores >= 3:
        finish = True
        text = font.render(WIN_TEXT, True, BLACK)

    if player.hitbox.colliderect(enemy.hitbox):
        finish = True
        text = font.render(LOSE_TEXT, True, BLACK)

    if player.hitbox.y > WINDOW_HEIGHT - 10:
        finish = True
        text = font.render(LOSE_TEXT, True, BLACK)

    return finish, text

def collisions(player, coins, scores):

    for coin in coins:
        if player.hitbox.colliderect(coin.hitbox):
            scores += 1
            coins.remove(coin)

    return scores

def draw_platforms(window, platforms):

    for platform in platforms:
        window.blit(platform.image, (platform.hitbox.x, platform.hitbox.y))

def draw_coins(window, coins):

    for coin in coins:
        window.blit(coin.image, (coin.hitbox.x, coin.hitbox.y))
        

        