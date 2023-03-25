import pygame
import os
from constants import*

pygame.init()

class Sprite():

    def __init__(self, width = 10, height = 10, x = 0, y = 0, img_name = "", speed = 0):
        self.hitbox = pygame.Rect(x, y, width, height)

        self.path = os.path.join(IMAGES_PATH, img_name)
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.speed = speed

        
        