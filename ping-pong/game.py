import pygame as pg
from random import randint

class Game():

    def create_objects(self):
       pass


    def draw_objects(self):
        pass

    def move_objects(self):

        pass

    def collisions(self):
        
        if self.ball.rect.colliderect(self.platform1.rect):
            self.dir_x = 1
            self.dir_y = randint(-1, 1)
            
        if self.ball.rect.colliderect(self.platform2.rect):
            self.dir_x = -1
            self.dir_y = randint(-1, 1)


        if self.ball.rect.y < 10: 
            self.dir_y = 1

    def win_lose(self):
       
        font = pg.font.Font

    
    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False
        
    def update_window(self):
        self.window.clock.tick(FPS)
        pg.display.update()

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
                self.collisions()
                self.win_lose()
                self.update_window()
                self.event_handler()

Game().game_loop()