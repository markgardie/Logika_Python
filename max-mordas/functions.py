import pygame
from constants import*
from player import*
from obstacle import*
from random import*

pygame.init()

def create_obstacles(obstacles, timer):

    chance = randint(1, 10)

    if chance == 1 and timer == 0:
        obstacle_variant = randint(1, 3)

        if obstacle_variant == 1:
            obstacle = Obstacle(CACTUS1_WIDTH, CACTUS_HEIGHT, WINDOW_WIDTH - 50, CACTUS_Y, CACTUS1_PATH, OBSTACLE_SPEED)
            obstacles.append(obstacle)

        if obstacle_variant == 2:
            obstacle = Obstacle(CACTUS2_WIDTH, CACTUS_HEIGHT, WINDOW_WIDTH - 100, CACTUS_Y, CACTUS2_PATH, OBSTACLE_SPEED)
            obstacles.append(obstacle)

        if obstacle_variant == 3:
            obstacle = Obstacle(PTERO_WIDTH, PTERO_HEIGHT, WINDOW_WIDTH - 50, PTERO_Y, PTERO_PATH, OBSTACLE_SPEED)
            obstacles.append(obstacle)

        timer = 240
    
    else:
        timer -= 1
        
        return obstacles, timer

def draw_obstacles(window, obstacles):

    for obstacle in obstacles:
        window.blit(obstacle.image, (obstacle.hitbox.x, obstacle.hitbox.y))

def move_obstacles(obstacles):

    for obstacle in obstacles:
        obstacle.move()


def colisions (player, obstacles, finish):

    for obstacle in obstacles:
    
        if player.hitbox.colliderect(obstacle.hitbox):

            finish = True

    return finish

def jump(player):
    if player.jumping:
        player.hitbox.y -= player.speed * 4
        player.speed -= 0.8

    if player.speed < -player.SPEEED:
        player.hitbox.y = PLAYER_Y
        player.jumping = False
        player.speed = player.SPEEED
    


def pbutton_clicked(luvel):
    return 2

def sbutton_clicked(luvel):
    return 3

def bbutton_clicked(luvel):
    return 2

def ebutton_clicked(game):
    return False


