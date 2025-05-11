from sprite import Sprite
from constants import*

class Card(Sprite):

    def __init__(self, width, height, x, y, color):
        super().__init__(width, height, x, y)
        self.color = color
        self.font = pg.font.Font(None, CLICK_TEXT_SIZE)
        self.text = self.font.render(CLICK_TEXT, True, BLACK)

    def set_color(self, new_color):
        self.color = new_color
       