import pygame

pygame.init()

class Sprite(pygame.sprite.Sprite):

    def __init__(self, width, height, image, x, y, speed):

        super().__init__()

        self.speed = speed

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    
