import pygame
from constants import*
import os

# Створення класу
pygame.init()

class Sprite():
    
    def __init__(self, width, height, x, y, img_name, speed):
        self.hitbox = pygame.Rect(x, y, width, height)
        self.speed = speed

        self.path = os.path.join(IMAGES_PATH, img_name)
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (width, height))

# Створення класу