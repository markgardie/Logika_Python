import pygame
import os
from constants import*

pygame.init()

class Sprite():

    def __init__(self, width = 10, height = 10, x = 0, y = 0, img_path = "", speed = 0):
        

        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

        self.speed = speed

        
        