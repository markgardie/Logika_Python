import pygame
from constants import*
from player import Player
from button import Button

class Game:

    def __init__(self):

        self.window = pygame.display.set_mode((WIN_W, WIN_H))
        pygame.display.set_caption(TITLE)

        self.player = Player(
            (PLAYER_X, PLAYER_Y),
            (PLAYER_SIZE, PLAYER_SIZE),
            C_PLAYER,
            PLAYER_SPEED
            )
        
        self.win_rect = pygame.Rect(
            WIN_RECT_X, WIN_RECT_X,
            TARGET_SIZE, TARGET_SIZE
        )

        self.lose_rect = pygame.Rect(
            LOSE_RECT_X, LOSE_RECT_X,
            TARGET_SIZE, TARGET_SIZE
        )

        self.start_button = Button(
            (BUTTON_X, BUTTON_y),
            (BUTTON_W, BUTTON_H),
            C_BTN,
            C_TEXT,
            None,
            20,
            "Почати гру"
        )

        self.scene = "menu"
        font = pygame.font.Font(None, 60)

        self.menu_title_text = font.render(TITLE, True, C_TEXT)
        self.lose_text = font.render("Ти програв", True, C_TEXT)
        self.win_text = font.render("Ти виграв", True, C_TEXT)


    def update(self):
        pass


    def draw(self):
        if self.scene == "menu":
            self.window.blit(
                self.menu_title_text, 
                (BUTTON_X, BUTTON_y - 30)
                )
            self.start_button.draw(self.window)
        # dz: game, win, lose

    def win_lose(self):
        if self.player.rect.colliderect(self.win_rect):
            self.scene = "win"

    def loop(self):
        # dz: while, quit, update, fill
        pass