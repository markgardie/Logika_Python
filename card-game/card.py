import os
import pygame
from constants import*

class Card():

    def __init__(self, x, y, width, height, img_name):
        self.x = x
        self.y = y 
        self.width = width 
        self.height = height 
        self.img_name = img_name
        self.image = None
        self.num =  None
        self.rect = pygame.Rect(x,y, width, height)

    def load_image(self):
        img_path = os.path.join(IMAGES_PATH, self.img_name)
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
