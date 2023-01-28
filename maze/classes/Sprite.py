import pygame

pygame.init()

class Sprite():

    def __init__(self, width,  height, image_path, x, y, speed):
        self.rect = pygame.Rect(x, y, width, height)

        self.speed = speed

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))

        #self.hitbox = self.image.get_rect()
        #self.hitbox.x = x
        #self.hitbox.y = y




