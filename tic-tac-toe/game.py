import pygame as pg
from constants import*
from window import Window

class Game():

    def create_objects(self):
        
        self.window = Window(
            WINDOW_WIDTH, WINDOW_HEIGHT,
            BG_IMAGE_PATH, CAPTION
        )
        
        self.player_id = 1

        self.map = [0, 0, 0,
                    0, 0, 0,
                    0, 0, 0]

        # дз: 9 комірок


    def draw_objects(self):
        # дз: 9 комірок
        pass

    def collisions(self, x, y):
        for cell in self.cells:
            if cell.rect.collidepoint(x, y):
                cell.click(self.player_id)

                if cell.empty:
                    self.map[self.cells.index(cell)] = self.player_id
                    if self.player_id == 1:
                        self.player_id = 2
                    else:
                        self.player_id = 1

    def win_lose(self):

        font = pg.font.Font(None, FONT_SIZE)

        if self.map[0] == self.map[1] and self.map[1] == self.map[2]:
            self.finish = True
            self.text = font.render(f"Переміг гравець: {self.player_id}")

    
    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                self.collisions(x, y)
        
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