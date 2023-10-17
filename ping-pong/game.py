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
        
        pass

    def win_lose(self):
       
        pass

    
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