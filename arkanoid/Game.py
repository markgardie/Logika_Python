from Constants import*
from Sprite import*
from Window import Window
from Platform import Platform
from Ball import Ball
from random import randint

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

        x = 20
        y = 20

        for row in MAP:
            for place in row:
                if place == "1":
                    block = Sprite(BLOCK_WIDTH, BLOCK_HEIGHT,
                                   x, y, BLOCK_IMAGE_PATH)
                x += 76
            y += 56
            x = 20        

    def draw_objects(self):
        self.window.screen.blit(self.platform.image, 
                                (self.platform.hitbox.x, self.platform.hitbox.y))
        
        self.window.screen.blit(self.ball.image, 
                                (self.ball.hitbox.x, self.ball.hitbox.y))
        
        for block in self.blocks:
            self.window.screen.blit(self.block.image, 
                                (self.block.hitbox.x, self.block.hitbox.y))

    def move_objects(self):

        self.dir_x = 1
        self.dir_y = -1

        self.platform.controls(pg.K_a, pg.K_d)
        self.ball.move(self.dir_x, self.dir_y)

    def collisions(self):
        
        if self.ball.hitbox.colliderect(self.platform.hitbox):
            self.dir_y = -1
            self.dir_x = randint(-1, 1)

        for block in self.blocks:
            if self.ball.hitbox.colliderect(self.block.hitbox):
                self.dir_y = 1
                self.dir_x = randint(-1, 1)
                self.blocks.remove(block)

        if self.ball.hitbox.x < 0:
            self.dir_x = 1  

    def win_lose(self):
        font = pg.font.Font(None, FONT_SIZE)

        if len(self.blocks) == 0:
            self.finish = True
            self.text = font.render(WIN_TEXT, True, BLACK)

        

    def update_window(self):
        self.window.clock.tick(FPS)
        pg.display.update()

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