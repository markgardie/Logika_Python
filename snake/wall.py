
import pyglet

class Wall():

    def __init__(self, x, y, cell_size):
        self.position = (x, y)
        self.cell_size = cell_size

        self.color = (139, 69, 19)

    def is_collisions(self):
        pass

    def draw(self):
        pass