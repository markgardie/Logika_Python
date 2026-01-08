from pygame.draw import circle

class Food():

    def __init__(self, x, y, radius, color, surface):
        circle(surface, color, (x, y), radius)