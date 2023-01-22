import pygame

pygame.init()

class Window():

    def __init__(self, width, height, caption, image_path):
        
        self.display = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.bg_image = pygame.image.load(image_path)
        self.bg_image = pygame.transform.scale(self.bg_image, (width, height))

        self.clock = pygame.time.Clock(