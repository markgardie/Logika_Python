import pygame as pg
from constants import*
from Enemy import*
from random import randint

def create_enemies():

    enemies = pg.sprite.Group()

    for i in range(ENEMY_NUMBER):
        
        x = randint(80, WINDOW_WIDTH - 80)
        speed = randint(1, 5)

        enemy = Enemy(ENEMY_WIDTH, ENEMY_HEGHT, x, ENEMY_Y, ENEMY_IMAGE_PATH, speed)

        enemies.add(enemy)

    return enemies

def collisions(enemies, bullets):

    collides = pg.sprite.groupcollide(enemies, bullets, True, True)

    for c in collides:
        scores[0] += 1

        x = randint(ENEMY_X_START, ENEMY_X_END)
        speed = randint(1, 5)

        enemy = Enemy(ENEMY_WIDTH, ENEMY_HEGHT, x, ENEMY_X_START, ENEMY_IMAGE_PATH, speed)

        enemies.add(enemy)

def win(finish, text):
    if scores[0] >= GOAL:
        finish = True

        font = pg.font.Font(None, 50)

        text = font.render(WIN_TEXT, True, TEXT_COLOR)

    return finish, text

def lose(finish, text):
    if miss[0] >= MAX_MISS:
        finish = True

        font = pg.font.Font(None, 50)

        text = font.render(LOSE_TEXT, True, TEXT_COLOR)
    
    return finish, text