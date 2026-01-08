from pygame import Rect
from pygame.image import load
from pygame.transform import scale

class Image_Sprite():

    def __init__(self, x, y, width, height, image_path):
        self.hitbox = Rect(x, y, width, height)
        self.texture = load(image_path)
        self.texture = scale(self.texture, (x, y))

    def draw(self, surface):
        surface.blit(self.texture, (self.hitbox.x, self.hitbox.y))