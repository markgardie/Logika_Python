import pygame

pygame.init()

class Sprite():
    
    def __init__(self, width, height, x, y, color, speed):

        self.hitbox = pygame.Rect(x, y, width, height)

        self.color = color
        self.speed = speed