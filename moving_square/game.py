import pygame
from constants import*
from player import Player
from button import Button

class Game:

    def __init__(self):
        pygame.font.init()

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

        # dz: return_button

        self.scene = "menu"
        font = pygame.font.Font(None, 60)

        self.running = True

        self.clock = pygame.time.Clock()

        self.menu_title_text = font.render(TITLE, True, C_TEXT)
        self.lose_text = font.render("Ти програв", True, C_TEXT)
        self.win_text = font.render("Ти виграв", True, C_TEXT)


    def click_button(self, event):
        if (self.scene == "menu"
            and event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.start_button.rect.collidepoint(event.pos)
            ):
            self.scene = "game"

        #dz: return_button

    def player_update(self):
        if self.scene == "game":
            self.player.update(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
        



    def draw(self):
        if self.scene == "menu":
            self.window.blit(
                self.menu_title_text, 
                (BUTTON_X, BUTTON_y - 30)
                )
            self.start_button.draw(self.window)
        if self.scene == "game":
            self.player.draw(self.window)
            pygame.draw.rect(self.window, C_WIN_RECT, self.win_rect)
            pygame.draw.rect(self.window, C_LOSE_RECT, self.lose_rect)
        if self.scene == "win":
            self.window.blit(
                self.win_text, 
                (
                    self.window.get_width() / 2 - self.win_text.get_width() / 2,
                    self.window.get_height() / 2 - self.win_text.get_height() / 2
                )
                )
                # draw return_button
        if self.scene == "lose":
            self.window.blit(
                self.lose_text, 
                (
                    self.window.get_width() / 2 - self.lose_text.get_width() / 2,
                    self.window.get_height() / 2 - self.lose_text.get_height() / 2
                )
                )
                # draw return_button



    def win_lose(self):
        if self.player.rect.colliderect(self.win_rect):
            self.scene = "win"
        if self.player.rect.colliderect(self.lose_rect):
            self.scene = "lose"

    def loop(self):
        # dz: while, quit, update, fill
        while self.running:
            for e in pygame.event.get():
                self.click_button(e)
                if e.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

            self.window.fill(C_BG)

            self.draw()
            self.player_update()
            self.win_lose()

            self.clock.tick(FPS)
            pygame.display.flip()

Game().loop()