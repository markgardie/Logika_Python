import pygame
from constants import*

class Sprite():

    def __init__(self, width = 10, height = 10, x = 0, y = 0, img_name = "", speed = 0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed
        self.img_name = img_name
        self.img_path = os.path.join(IMAGES_PATH, img_name)
        self.image = None
        self.hitbox = pygame.Rect(x, y, width, height)

    def load_image(self):
        image = pygame.image.load(self.img_path)
        self.image = pygame.transform.scale(image, (self.hitbox.width, self.hitbox.height))

    def move_left(self):
        self.x -= self.speed
        self.hitbox.x -= self.speed

    def move_right(self):
        self.x += self.speed
        self.hitbox.x += self.speed