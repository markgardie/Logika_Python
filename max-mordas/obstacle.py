from sprite import*
from constants import*
import pygame

pygame.init()

# Спадкує клас"Obstacle" від класу "Sprite"
class Obstacle(Sprite):
    # Функція "Рух"
    def move(self):
        self.hitbox.x -= self.speed