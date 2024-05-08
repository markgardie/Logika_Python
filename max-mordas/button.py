import pygame
from sprite import*


class Button(Sprite):
    def __init__(self, width, height, x, y, img_name, speed, action):
        super().__init__(width, height, x, y, img_name, speed)
        self.action = action

    def check_click(self, mouse_pos, argument):
        if self.hitbox.collidepoint(mouse_pos):
            return self.action(argument)