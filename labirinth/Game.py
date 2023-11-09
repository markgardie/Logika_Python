import pygame as pg
from Sprite import Sprite
from Window import Window
from Player import Player
from Enemy import Enemy
from Constants import *
from Wall import Wall

class Game():

    def create_objects(self):

        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_CAPTION, BACKGROUND_PATH)

        self.player = Player(SPRITE_WIDTH, SPRITE_HEIGHT,
                             PLAYER_X, PLAYER_Y,
                             PLAYER_PATH, PLAYER_SPEED)
        
        self.goal = Sprite(SPRITE_WIDTH, SPRITE_HEIGHT,
                           GOAL_X, GOAL_Y,
                           GOAL_PATH, GOAL_SPEED)
        
        self.enemy = Enemy(SPRITE_WIDTH, SPRITE_HEIGHT,
                           MONSTER_X, MONSTER_Y,
                           MONSTER_PATH, MONSTER_SPEED)
        
        self.wall1 = Wall(WALL_COLOR1, WALL_COLOR2, WALL_COLOR3, 
                          WALL_X, WALL1_Y, 
                          WALL1_WIDTH, WALL1_HEIGHT
                          )
        
        self.wall2 = Wall(WALL_COLOR1, WALL_COLOR2, WALL_COLOR3, 
                          WALL_X, WALL2_Y, 
                          WALL2_WIDTH, WALL2_HEIGHT
                          )
        
        self.wall3 = Wall(WALL_COLOR1, WALL_COLOR2, WALL_COLOR3, 
                          WALL_X, WALL3_Y, 
                          WALL3_WIDTH, WALL3_HEIGHT
                          )

    def draw_objects(self):
        self.window.screen.blit(self.window.image, (0, 0))
        self.window.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        self.window.screen.blit(self.goal.image, (self.goal.rect.x, self.goal.rect.y))
        self.window.screen.blit(self.enemy.image, (self.enemy.rect.x, self.enemy.rect.y))
        self.window.screen.blit(self.wall1.image, (self.wall1.rect.x, self.wall1.rect.y))
        self.window.screen.blit(self.wall2.image, (self.wall2.rect.x, self.wall2.rect.y))
        self.window.screen.blit(self.wall3.image, (self.wall3.rect.x, self.wall3.rect.y))

    def move_objects(self):
        self.player.controls(pg.K_a, pg.K_d, pg.K_w, pg.K_s)
        self.enemy.move()


    def win_lose(self):

        font = pg.font.Font(None, FONT_SIZE)

        if (self.player.rect.colliderect(self.enemy.rect)
        or self.player.rect.colliderect(self.wall1.rect)
        or self.player.rect.colliderect(self.wall2.rect)
        or self.player.rect.colliderect(self.wall3.rect)):
            self.finish = True
            self.text = font.render(LOSE_TEXT, True, BLACK)
        

        if self.player.rect.colliderect(self.goal.rect):
            self.finish = True
            self.text = font.render(WIN_TEXT, True, BLACK)

    def update_window(self):
        self.window.clock.tick(FPS)
        pg.display.update()

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game = False

    def game_loop(self):
        self.create_objects()
        self.game = True
        self.finish = False

        while self.game:
            if self.finish:
                self.window.screen.blit(self.text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
                self.update_window()
                self.event_handler()
            else:
                self.draw_objects()
                self.move_objects()
                self.win_lose()
                self.update_window()
                self.event_handler()

Game().game_loop()