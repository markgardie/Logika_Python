import pygame

pygame.init()

class Sprite(pygame.sprite.Sprite):

    def __init__(self, width, height, image, x, y, speed):

        super().__init__()

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.speed = speed

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))

    def control(self, left, right, up, down):

        self.key_pressed = pygame.key.get_pressed()

        if  self.key_pressed[left] and self.x > 5:
            self.x -= self.speed
        if self.key_pressed[right] and self.x < 595:
            self.x += self.speed
        if self.key_pressed[up] and self.y > 5:
            self.y -= self.speed
        if self.key_pressed[down] and self.y < 395:
            self.y += self.speed
