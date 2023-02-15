import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, image_path, speed):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(pygame.image.load(image_path), (width, height))
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
