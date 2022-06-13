from constants import*
import pygame

pygame.init()

#------Window

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Card Game")


fps = pygame.time.Clock()

#------Game Cycle
game = True


while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            
    pygame.display.flip()
    window.fill(BLUE)
    fps.tick(60)
