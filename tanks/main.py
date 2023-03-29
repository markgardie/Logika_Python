from Tank import *
from Window import*
from functions import*
from Bullet import*
from constants import*
import time

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, BLUE, CAPTION)

tank1 = Tank(TANK_WIDTH, TANK_HEIGHT, TANK1_X, TANKS_Y, TANK1_IMAGE_PATH, PLAYER_SPEED)
tank2 = Tank(TANK_WIDTH, TANK_HEIGHT, TANK2_X, TANKS_Y, TANK2_IMAGE_PATH, PLAYER_SPEED)

bullets1 = []
bullets2 = []

game = True
finish = False
text = ""

while game:

    # цикл перебирає виникаючі події
    for event in pygame.event.get():
        # подія натискання на крестик
        if event.type == pygame.QUIT:
            # закриття гри та вікна при натисканні на крестик
            game = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            tank1.fire1(bullets1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            tank2.fire2(bullets2)


    if not finish:

        window.screen.blit(tank1.image, (tank1.hitbox.x, tank1.hitbox.y))
        window.screen.blit(tank2.image, (tank2.hitbox.x, tank2.hitbox.y))
        draw_bullets(window.screen, bullets1, bullets2)

        move_bullets(bullets1, bullets2)
        tank1.controls(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        tank2.controls(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)

        finish, text = win_lose(tank1, tank2, bullets1, bullets2)

    else:

        window.screen.blit(text, (WINDOW_WIDTH / 2 - 150, WINDOW_HEIGHT / 2 - 80))

    pygame.display.flip()
    window.screen.fill(BLUE)
    window.clock.tick(FPS)