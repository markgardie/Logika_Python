from image_sprite import Image_Sprite
from pygame.key import get_pressed

class Player(Image_Sprite):

    def __init__(self, x, y, width, height, image_path):
        super().__init__(x, y, width, height, image_path)
        self.size = 1

    def controls(self, key_up, key_down, key_left, key_right, speed):
        pressed_keys = get_pressed()

        if pressed_keys[key_up]:
            self.hitbox.y -= speed
        if pressed_keys[key_down]:
            self.hitbox.y += speed
        if pressed_keys[key_left]:
            self.hitbox.x -= speed
        if pressed_keys[key_right]:
            self.hitbox.x += speed


