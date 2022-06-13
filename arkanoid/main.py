from constants import*
import pygame

pygame.init()

#------Window

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Arkanoid")
icon = pygame.image.load(ICON_PATH)
pygame.display.set_icon(icon)

fps = pygame.time.Clock()

#------Blocks List
blocks = list()

#------Game Cycle
game = True


while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            
    pygame.display.flip()
    window.fill(BLUE)
    fps.tick(60)
