from functions import*
from constants import*
import pygame
from sprite import*

pygame.init()

#------Window

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Arkanoid")
icon = pygame.image.load(ICON_PATH)
pygame.display.set_icon(icon)

fps = pygame.time.Clock()

#------Create Sprites
blocks = list()
create_blocks(blocks)

platform = Sprite(PLATFORM_WIDTH, PLATFORM_HEIGHT, WINDOW_WIDTH / 2, WINDOW_HEIGHT - 30, "platform.png", speed=PLATFORM_SPEED)
platform.load_image()

ball = Sprite(BALL_WIDTH, BALL_HEIGHT, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, "ball.png", speed=BALL_SPEED)
ball.load_image()

#------Game Cycle
game = True
direction_y = 1
direction_x = 1

while game:

    draw_blocks(blocks, window)
    window.blit(platform.image, (platform.x, platform.y))
    window.blit(ball.image, (ball.x, ball.y))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False
        
    platform.handle_keys()

    direction_y, direction_x = handle_collisions(blocks, platform, ball, direction_y, direction_x)

    ball.move_diagonal(direction_y, direction_x)

       
    pygame.display.flip()
    window.fill(BLUE)
    fps.tick(60)
