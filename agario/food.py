from pygame.draw import circle

class Food():

    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        
    def draw(self, surface): 
        circle(surface, self.color, (self.x, self.y), self.radius)