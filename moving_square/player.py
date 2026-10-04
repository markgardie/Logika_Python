import pygame
from constants import*


class Player:

    def __init__(self, coords, size, color, speed):
        self.rect = pygame.Rect(
            coords[0],
            coords[1],
            size[0],
            size[1]
            )

        self.color = color
        self.speed = speed


    def update(self, up_key, down_key, left_key, right_key):
        keys = pygame.key.get_pressed()

        if keys[up_key] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.y < WIN_H:
            self.rect.y += self.speed
        if keys[left_key] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[right_key] and self.rect.x < WIN_W:
            self.rect.x += self.speed
        

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)