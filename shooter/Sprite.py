import pygame

pygame.init()

class Sprite():
    
    def __init__(self, width, height, x, y, image_path):

        self.hitbox = pygame.Rect(x, y, width, height)

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))