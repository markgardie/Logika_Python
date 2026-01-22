from pygame.draw import circle
from pygame import Rect

class Food():

    def __init__(self, x, y, radius, color):
        self.hitbox = Rect(x, y, radius*2, radius*2)
        self.radius = radius
        self.color = color
        
    def draw(self, surface): 
        circle(surface, self.color, (self.x, self.y), self.radius)