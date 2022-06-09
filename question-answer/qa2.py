from tkinter.tix import WINDOW
import pygame

pygame.init()

#----------Constants

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BUTTON_WIDTH = 290
BUTTON_HEIGHT = 70

BLUE = (0, 0, 250)
GREEN = (0, 250, 0)
BLACK = (255, 255, 255)


#----------Create Window

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Game")
fps = pygame.time.Clock()


#----------Button class

class Button:

    def __init__(self, width, height, x, y, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)


#----------Game Cycle

game = True

while game:

    pygame.display.flip()
    window.fill(BLUE)
    fps.tick(60) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False