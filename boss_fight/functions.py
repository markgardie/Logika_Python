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