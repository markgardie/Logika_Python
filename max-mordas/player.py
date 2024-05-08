from sprite import*
from constants import*
import pygame

pygame.init()

# Спадкує клас"Player" від класу "Sprite"
class Player(Sprite):
    def __init__(self, width, height, x, y, img_name, speed):
        super().__init__(width, height, x, y, img_name, speed)
        self.jumping = False
        self.jump_height = 30
        self.jump_number = self.jump_height
        self.SPEEED = self.speed

    # Функція "Керування"
    def controls(self, up):
        key_pressed = pygame.key.get_pressed()
    
        # Рух вгору
        if key_pressed[up] and  self.hitbox.y  > 5:
            self.jumping = True