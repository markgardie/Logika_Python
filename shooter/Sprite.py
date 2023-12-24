import pygame

pygame.init()

pygame.sprite.Group

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, width, height, x, y, image_path, speed):

        self.rect = pygame.Rect(x, y, width, height)

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.speed = speed