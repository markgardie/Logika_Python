# window.py

from pygame.display import set_mode, set_caption, update
from pygame.time import Clock
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, COLOR_WHITE


class Window:
    
    def __init__(self):
        self.surface = set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        set_caption("Agario Game")
        self.clock = Clock()
        self.fps = FPS
    
    def fill(self, color=COLOR_WHITE):
        self.surface.fill(color)
    
    def update(self):
        update()
        self.clock.tick(self.fps)