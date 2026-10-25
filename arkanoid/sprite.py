import pygame
import constants as const


class Sprite:

    def __init__(self, coords, size, speed, image_path):
        self.rect = pygame.Rect(
            coords[0],
            coords[1],
            size[0],
            size[1]
            )

        self.speed = speed

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (size[0], size[1]))


    def update(self):
        pass
        

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))