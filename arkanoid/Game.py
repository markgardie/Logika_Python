from Window import Window
from Sprite import Sprite
from Platform import Platform
from Ball import Ball
from Constants import*


class Game():

    def create_objects(self):

        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE)

        self.platform = Platform(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 30, 
                                 PLATFORM_WIDTH, PLATFORM_HEIGHT,
                                 PLATFORM_IMAGE_PATH)
        
        self.ball = Ball(WINDOW_WIDTH / 2, WINDOW_HEIGHT /2, 
                                 BALL_WIDTH, BALL_HEIGHT,
                                 BALL_IMAGE_PATH)
        
        self.blocks = self.create_blocks()
    
    def create_blocks(self):
        blocks = []

        x = 20
        y = 20

        for row in MAP:
            for place in row:
                if place == "1":
                    block = Sprite(x, y, BLOCK_WIDTH, BLOCK_HEIGHT, BLOCK_IMAGE_PATH)
                    blocks.append(block)

                x += 76

            y += 56
            x = 20

        
        return blocks
    
    def game_loop(self):

        self.game = True
        self.finish = False

        while self.game:
            self.draw_objects()
            self.move_objects()
            self.collisions()
            self.event_handler()
            self.win_lose()


