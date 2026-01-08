from pygame.display import set_mode, set_caption, update
from pygame.image import load
from pygame.transform import scale
from pygame.time import Clock

class Window():

    def __init__(self, width, height, caption, bg_image_path, fps):
        self.surface = set_mode((width, height))
        set_caption(caption)
        self.image = load(bg_image_path)
        self.image = scale(self.image, (width, height))
        self.clock = Clock()
        self.fps = fps

    def draw(self):
        self.surface.blit(self.image)
        self.clock.tick(self.fps)
        update()


