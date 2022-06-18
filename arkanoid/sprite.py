from constants import*
import pygame

class Sprite():

    def __init__(self, width, height, x, y, img_name):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.img_name = img_name

        self.image = None
        self.img_path = os.path.join(IMAGES_PATH, img_name)
        self.hitbox = pygame.Rect(x, y, width, height)
