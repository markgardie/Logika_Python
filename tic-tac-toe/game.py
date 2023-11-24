import pygame as pg
from constants import*
from window import Window
from cell import Cell

pg.init()
font = pg.font.Font(None, FONT_SIZE)

class Game():

    def create_objects(self):
        
        self.window = Window(
            WINDOW_WIDTH, WINDOW_HEIGHT,
            BG_COLOR, CAPTION
        )
        
        self.player_id = 1

        self.cells = []
        self.empty_cells = 9
        self.create_cells()

    def create_cells(self):
        x = FIRST_CELL_X
        y = FIRST_CELL_Y

        for i in range(3):
            for j in range(3):
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
                    cell.click(self.player_id)
                    self.empty_cells -= 1
                    if self.player_id == 1:
                        self.player_id = 2
                    else:
                        self.player_id = 1

                

    def win_lose(self):

        if (
            self.cells[0].filled != 0 and
            self.cells[0].filled == self.cells[1].filled and 
            self.cells[1].filled == self.cells[2].filled
        ):
            
            self.finish = True
            self.create_final_text()

        if (
            self.cells[3].filled != 0 and
            self.cells[3].filled == self.cells[4].filled and 
            self.cells[4].filled == self.cells[5].filled
        ):
            
            self.finish = True
            self.create_final_text()

        if (
            self.cells[6].filled != 0 and
            self.cells[6].filled == self.cells[7].filled and 
            self.cells[7].filled == self.cells[8].filled
        ):
            
            self.finish = True
            self.create_final_text()

        if (
            self.cells[0].filled != 0 and
            self.cells[0].filled == self.cells[3].filled and 
            self.cells[3].filled == self.cells[6].filled
        ):
            
            self.finish = True
            self.create_final_text()

        if (
            self.cells[1].filled != 0 and
            self.cells[1].filled == self.cells[4].filled and 
            self.cells[4].filled == self.cells[7].filled
        ):
            
            self.finish = True
            self.create_final_text()

        if (
            self.cells[2].filled != 0 and
            self.cells[2].filled == self.cells[5].filled and 
            self.cells[5].filled == self.cells[8].filled
        ):
            
            self.finish = True
            self.create_final_text()

        if (
            self.cells[0].filled != 0 and
            self.cells[0].filled == self.cells[4].filled and 
            self.cells[4].filled == self.cells[8].filled
        ):
            
            self.finish = True
            self.create_final_text()

        if (
            self.cells[2].filled != 0 and
            self.cells[2].filled == self.cells[4].filled and 
            self.cells[4].filled == self.cells[6].filled
        ):
            
            self.finish = True
            self.create_final_text()

        if self.empty_cells == 0:
            self.finish = True
            self.text = font.render(f"Нічия", True, BLACK)


    def create_final_text(self):
        if self.player_id == 1:
            self.player_id = 2
        else: 
            self.player_id = 1

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
                self.window.screen.blit(self.text, (WINDOW_WIDTH / 2 - 200, WINDOW_HEIGHT / 2 - 100))
                self.update_window()
                self.event_handler()
            else:
                self.update_window()
                self.win_lose()
                self.draw_objects()
                self.event_handler()

Game().game_loop()