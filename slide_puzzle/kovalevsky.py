from constants import*
import pygame

pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Slide Puzzle")


fps = pygame.time.Clock()
pygame.display.flip()
window.fill(BLACK)
fps.tick(60)


game = True

while game:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False

    pygame.display.flip()
    window.fill(BLACK)
    fps.tick(60)
