from constants import*
import pygame

player_hp = 3
boss_hp = 3

def win_lose():
    global player_hp
    global boss_hp

    finish = False
    text = ""

    font = pygame.font.Font(None, 50)

    if player_hp == 0:
        finish = True
        text = font.render("Поразка", True, BLACK)

    if boss_hp == 0:
        finish = True
        text = font.render("Перемога", True, BLACK)

    return finish, text

def draw_fireballs(window, fireballs):
    for fireball in fireballs:
        window.blit(fireball.image, (fireball.hitbox.x, fireball.hitbox.y))

def move_fireballs(fireballs):  
    for fireball in fireballs:
        fireball.move()

def collisions(player, fireballs, boss):

    global player_hp
    global boss_hp

    for fireball in fireballs:
        if player.hitbox.colliderect(fireball.hitbox):
            player_hp -= 1
            fireballs.remove(fireball)

    if player.hitbox.colliderect(boss.hitbox):
            boss_hp -= 1
            boss.move()