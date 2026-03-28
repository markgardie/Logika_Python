from Tank import *
from Window import*
from functions import*
from Bullet import*
from constants import*
import time

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, BLUE, CAPTION)

tank1 = Tank(TANK_WIDTH, TANK_HEIGHT, TANK1_X, TANKS_Y, TANK1_IMAGE_PATH, PLAYER_SPEED)
tank2 = Tank(TANK_WIDTH, TANK_HEIGHT, TANK2_X, TANKS_Y, TANK2_IMAGE_PATH, PLAYER_SPEED)

wall1 = Sprite(V_WALL_WIDTH, V_WALL_HEIGHT, WALL1_X, WALL1_Y, WALL_IMAGE_PATH, WALL_SPEED)
wall2 = Sprite(V_WALL_WIDTH, V_WALL_HEIGHT, WALL2_X, WALL2_Y, WALL_IMAGE_PATH, WALL_SPEED)

wall3 = Sprite(H_WALL_WIDTH, H_WALL_HEIGHT, WALL3_X, WALL3_Y, WALL_IMAGE_PATH, WALL_SPEED)
wall4 = Sprite(H_WALL_WIDTH, H_WALL_HEIGHT, WALL4_X, WALL4_Y, WALL_IMAGE_PATH, WALL_SPEED)

bullets1 = []
bullets2 = []

walls = [wall1, wall2, wall3, wall4]

game = True
finish = False
text = ""

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            tank1.fire1(bullets1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            tank2.fire2(bullets2)

    if not finish:
        
        window.screen.blit(tank1.image, (tank1.hitbox.x, tank1.hitbox.y))
        window.screen.blit(tank2.image, (tank2.hitbox.x, tank2.hitbox.y))
        draw_bullets(window.screen, bullets1, bullets2)

        window.screen.blit(wall1.image, (wall1.hitbox.x, wall1.hitbox.y))
        window.screen.blit(wall2.image, (wall2.hitbox.x, wall2.hitbox.y))
        window.screen.blit(wall3.image, (wall3.hitbox.x, wall3.hitbox.y))
        window.screen.blit(wall4.image, (wall4.hitbox.x, wall4.hitbox.y))

        move_bullets(bullets1, bullets2)

        wall_collisions(walls, bullets1, bullets2)

        tank1.controls(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        tank2.controls(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)

        finish, text = win_lose(tank1, tank2, bullets1, bullets2, walls)

    else:
        window.screen.blit(text, (WINDOW_WIDTH / 2 - 150, WINDOW_HEIGHT / 2 - 80))

    pygame.display.flip()
    window.screen.fill(BLUE)
    window.clock.tick(FPS)