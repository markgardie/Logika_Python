from Window import Window
from Sprite import Sprite
from Dino import Dino
from Obstacle import Obstacle
from Constants import*
import pygame as pg
from random import randint

class Game():

    def create_objects(self):

        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE)

        self.dino = Dino(
            DINO_X, DINO_Y,
            DINO_WIDTH, DINO_HEIGHT,
            STAND_IMAGE_PATH, DINO_SPEED
        )

    def create_obstacles(self):

        self.obstacle = None

        if self.obstacle == None:

            obstacle_type = randint(0, 1)

            if obstacle_type == 0:
                self.obstacle = Obstacle(CACTUS_X, CACTUS_Y, 
                                CACTUS_WIDTH, CACTUS_HEIGHT, 
                                CACTUS_IMAGE_PATH, OBSTACLE_SPEED)
                
            if obstacle_type == 1:
                self.obstacle = Obstacle(BAT_X, BAT_Y, 
                                BAT_WIDTH, BAT_HEIGHT, 
                                BAT_IMAGE_PATH, OBSTACLE_SPEED)
                
    def destroy_obstacles(self):

        if self.obstacle.hitbox.x < 0:
            self.obstacle = None
    
    def game_loop(self):

        self.game = True
        self.finish = False

        self.create_objects()

        while self.game:
            if self.finish: 
                self.window.screen.blit(self.final_text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
            else:
                self.create_obstacles()
                self.destroy_obstacles()
                self.draw_objects()
                self.move_objects()
                self.collisions()
                self.event_handler()
                self.win_lose()

    def draw_objects(self):
        self.window.screen.blit(self.dino.image, 
                                (self.dino.hitbox.x, self.dino.hitbox.y))
        
        self.window.screen.blit(self.obstacle.image, 
                                (self.obstacle.hitbox.x, self.obstacle.hitbox.y))

    def move_objects(self):

       self.dino.jump()
       self.obstacle.move()

    def collisions(self):
        
       pass

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game = False

    def win_lose(self):
        pass
        # font = pg.font.Font(None, FONT_SIZE)

        # if len(self.blocks) == 0:
        #     self.finish = True
        #     self.final_text = font.render(WIN_TEXT, True, BLACK)

        # if self.ball.hitbox.y > WINDOW_HEIGHT:
        #     self.finish = True
        #     self.final_text = font.render(LOSE_TEXT, True, BLACK)

Game().game_loop()