import pygame
from constants import*

class Sprite():

    def __init__(self, width = 10, height = 10, x = 0, y = 0, img_name = "", speed = 0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.img_name = img_name
        self.speed = speed

        self.img_path = os.path.join(IMAGES_PATH, img_name)
        self.image = None
        self.hitbox = pygame.Rect(x, y, width, height)

    def load_image(self):
        image = pygame.image.load(self.img_path)
        self.image = pygame.transform.scale(image, (self.hitbox.width, self.hitbox.height))

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move_left()
        if keys[pygame.K_d]:
            self.move_right()
    
    def move_left(self):
        self.x -= self.speed
        self.hitbox.x -= self.speed

    def move_right(self):
        self.x += self.speed 
        self.hitbox.x += self.speed

    def move_diagonal(self, direction_y, direction_x):
        self.y += self.speed * direction_y
        self.hitbox.y += self.speed * direction_y

        self.x += self.speed * direction_x
        self.hitbox.x += self.speed * direction_x

