import pygame

pygame.init()

class Window():

    def __init__(self, width, height, caption, bg_path):

        self.screen = pygame.display.set_mode((width, height))
        
        pygame.display.set_caption(caption)

        self.image = pygame.image.load(bg_path)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.clock = pygame.time.Clock()