

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
        pass
        
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
            else:
                self.draw_objects()
                self.move_objects()
                self.collisions()
                self.win_lose()
                self.update_window()

Game().game_loop()