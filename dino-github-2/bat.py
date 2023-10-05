import pygame

from load_sprites import load_image

class Bat(pygame.sprite.Sprite):

    def __init__(self, x=600, y=180):
        super(Bat, self).__init__()
     
        self.images = [
            load_image('bat1.png'),
            load_image('bat2.png')
        ]
        self.index = 0
        self.image = self.images[self.index]

        self.speed_x = -10
        self.speed_y = 0
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(self.x, self.y, 43, 34)

    def update(self):
        self.rect.move_ip(self.speed_x, self.speed_y)
        
        if self.rect.left < -10:
            self.rect = pygame.rect.Rect(self.x, self.y, 43, 34)

        if(self.speed_x != 0):
            self.index += 1
            if self.index == len(self.images):
                self.index = 0
            self.image = self.images[self.index]

    def stop(self):
        self.speed_x = 0
        self.index = 0
        self.image = self.images[self.index]