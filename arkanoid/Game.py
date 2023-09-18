from Constants import*
from Sprite import*
from Window import Window
from Platform import Platform
from Ball import Ball

class Game():

    def create_objects(self):
        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE)

        self.platform = Platform(PLATFORM_WIDTH, PLATFORM_HEIGHT, 
                                 WINDOW_WIDTH / 2, WINDOW_HEIGHT - 30,
                                 PLATFORM_IMAGE_PATH)
        
        self.ball = Ball(BALL_WIDTH, BALL_HEIGHT, 
                                 WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                                 BALL_IMAGE_PATH)
        
        self.blocks = self.create_blocks()

    def create_blocks(self):
        for row in MAP:
            for place in row:
                if place == "1":
                    pass #TODO

    def draw_objects(self):
        pass

    def move_objects(self):
        pass

    def collisions(self):
        pass


    def win_lose(self):
        pass

    def update_window(self):
        pass

    def game_loop(self):
        self.create_objects()
        self.game = True
        self.finish = False

        while self.game:
            self.draw_objects()
            self.move_objects()
            self.collisions()
            self.win_lose()
            self.update_window()