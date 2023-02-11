import pygame

pygame.init()

class Sprite():

    def __init__(self, width = 10, height = 10, x = 0, y = 0, img_name = "", speed = 0):
        self.hitbox = pygame.Rect(x, y, width, height)

        
        