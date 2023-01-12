import pygame

pygame.init()

class Sprite():

    def __init__(self, width,  height, image_path, x, y, speed):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))



