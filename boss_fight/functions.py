from constants import*
import pygame


def win_lose(player_hp, boss_hp):

    finish = False
    text = ""

    font = pygame.font.Font(None, 50)

    if player_hp <= 0:
        finish = True
        text = font.render("Програш", True, BLACK)

    if boss_hp <= 0:
        finish = True
        text = font.render("Виграш", True, BLACK)

    return finish, text

def draw_fireballs(window, fireballs):

    for fireball in fireballs:
        window.blit(fireball.image, (fireball.hitbox.x, fireball.hitbox.y))

def move_fireballs(fireballs):
    for fireball in fireballs:
        fireball.move()

def collisions(player, boss, fireballs, player_hp, boss_hp):


    for fireball in fireballs:

        if player.hitbox.colliderect(fireball.hitbox):
            player_hp -= 1
            fireballs.remove(fireball)

    if player.hitbox.colliderect(boss.hitbox):
        boss_hp -= 1
        boss.move()

    return player_hp, boss_hp
