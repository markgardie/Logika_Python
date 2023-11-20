import pygame as pg
from constants import*
from window import Window
from cell import Cell

pg.init()

class Game():

    def create_objects(self):
        
        self.window = Window(
            WINDOW_WIDTH, WINDOW_HEIGHT,
            BG_COLOR, CAPTION
        )
        
        self.player_id = 1

        self.map = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]

        self.cells = []
        self.create_cells()

    def create_cells(self):
        x = FIRST_CELL_X
        y = FIRST_CELL_Y

        for row in self.map:
            for place in row:
                cell = Cell(
                    CELL_WIDTH, CELL_HEIGHT,
                    START_IMAGE_PATH, CROSS_IMAGE_PATH, ZERO_IMAGE_PATH,
                    x, y
                )
                self.cells.append(cell)
                x += X_STEP
            x = FIRST_CELL_X
            y += Y_STEP

    def draw_objects(self):
        for cell in self.cells:
            self.window.screen.blit(cell.image, (cell.rect.x, cell.rect.y)) 

    def collisions(self, x, y):
        for cell in self.cells:
            if cell.rect.collidepoint(x, y):

                if cell.empty:
                    self.map[self.cells.index(cell)] = self.player_id
                    if self.player_id == 1:
                        self.player_id = 2
                    else:
                        self.player_id = 1

                cell.click(self.player_id)

               

    def win_lose(self):

        font = pg.font.Font(None, FONT_SIZE)

        if self.map[0][0] == self.map[0][1] and self.map[0][1] == self.map[0][2]:
            self.finish = True
            self.text = font.render(f"Переміг гравець: {self.player_id}", True, BLACK)

    
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
                self.update_window()
                self.event_handler()
            else:
                self.draw_objects()
                self.update_window()
                self.event_handler()

Game().game_loop()