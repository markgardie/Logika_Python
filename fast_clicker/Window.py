import pygame

pygame.init()

class Window():

    def __init__(self, width, height, bg_color, caption):

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.screen.fill(bg_color)

        self.clock = pygame.time.Clock()