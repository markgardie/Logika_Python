import pygame

pygame.init()

class Window():

    # конструктор
    def __init__(self, width, height, caption, background):

        # створює вікно
        self.screen = pygame.display.set_mode((width, height))
        
        pygame.display.set_caption(caption)

        self.screen.fill(background)

        self.clock = pygame.time.Clock()