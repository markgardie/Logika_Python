
COUNTER_TEXT = "Бали:"

class Counter():
    
    def __init__(self):

        self.scores = 0

        self.font = pg.font.Font(None, COUNTER_TEXT_SIZE)
        self.text = self.font.render(COUNTER_TEXT + self.scores, True, BLACK)