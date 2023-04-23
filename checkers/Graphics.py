import pygame as pg
from constants import*

pg.init()


class Graphics():

    def __init__(self):
        self.caption = CAPTION

        self.fps = FPS

        self.window_size = WINDOW_SIZE

        self.screen = pg.display.set_mode((self.window_size, self.window_size))
        # завантажити зображення для фону

        self.square_size = self.window_size / 8
        self.piece_size = self.square_size / 2

        self.message = False

    def setup_window():
        # ініціалізувати, запустити pygame
        # виставити надпис вікна

    def update_display(self, board, legal_moves, selected_piece):

        # blit, намалювати фон в координатах 0, 0
        # оновлення екрана, вікна
        # тіки годинника