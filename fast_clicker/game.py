from constants import *
from sprite import Sprite
from window import Window
from card import Card
from label import Label
from random import randint
import pygame as pg
from time import time

class Game():

    def __init__(self):
        self.timer = 0
        self.scores = 0  
        self.start_time = time()
        self.goal_card = 0
        self.end_time = 0
        self.finish = False 
        self.game = True 
        self.text = None 

        pg.font.init()

    def create_objects(self):
        self.main_window = Window(
            WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE
        )
        
        self.cards = self.create_cards()
        
        self.score_label = Label(
            SCORES_TEXT_COR[0], SCORES_TEXT_COR[1], 
            SCORES_TEXT_SIZE, TEXT_COLOR, 
            f"{SCORES_TEXT} {self.scores}"
        )

    def create_cards(self):
        cards = []
        x = START_X

        for i in range(CARDS_NUM):
            new_card = Card(
                CARD_WIDTH, CARD_HEIGHT,
                x, CARDS_Y, YELLOW
            )

            cards.append(new_card)

            x += CARDS_DISTANCE

        return cards
        
    def draw_objects(self):
        self.main_window.background.fill(BLUE)  
        self.draw_cards()
     
        self.score_label.change_text(f"{SCORES_TEXT} {self.scores}")
        self.main_window.background.blit(self.score_label.text, (self.score_label.x, self.score_label.y))

    def draw_cards(self):
        if self.timer == 0:
            self.timer = 60
            self.goal_card = randint(0, len(self.cards) - 1)

            for card in self.cards:
                card.set_color(YELLOW)

                pg.draw.rect(self.main_window.background, card.color, card.hitbox)
                pg.draw.rect(self.main_window.background, BLUE, card.hitbox, OUTLINE_THICKNESS)

                if self.cards.index(card) == self.goal_card:
                    self.main_window.background.blit(card.text, 
                                          (card.hitbox.x + TEXT_X_SHIFT, 
                                           card.hitbox.y + TEXT_Y_SHIFT
                                           )
                                          )
        else:
            self.timer -= 1
            
            for card in self.cards:
                pg.draw.rect(self.main_window.background, card.color, card.hitbox)
                pg.draw.rect(self.main_window.background, BLUE, card.hitbox, OUTLINE_THICKNESS)
                
                if self.cards.index(card) == self.goal_card:
                    self.main_window.background.blit(card.text, 
                                          (card.hitbox.x + TEXT_X_SHIFT, 
                                           card.hitbox.y + TEXT_Y_SHIFT
                                           )
                                          )


    def click(self, e):
        x, y = e.pos
        for card in self.cards:
            if card.hitbox.collidepoint(x, y):
                if self.cards.index(card) == self.goal_card:
                    card.set_color(GREEN)
                    self.scores += 1
                else:
                    card.set_color(RED)
                    self.scores -= 1

                pg.draw.rect(self.main_window.background, card.color, card.hitbox)

    def win_lose(self):
        self.end_time = time()
        font = pg.font.Font(FINAL_TEXT_FONT, FINAL_TEXT_SIZE)

        if self.end_time - self.start_time >= 11:
            self.text = font.render(LOSE_TEXT, True, TEXT_COLOR)
            self.finish = True
        
        if self.scores > 5: 
            self.text = font.render(WIN_TEXT, True, TEXT_COLOR)
            self.finish = True

    def update_window(self):
        self.main_window.clock.tick(FPS) 
        pg.display.update()

    def event_handler(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.game = False
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                self.click(e)

    def game_loop(self):
        self.create_objects()
        self.game = True
        self.finish = False

        while self.game:
            self.event_handler()
            
            if self.finish:
                self.main_window.background.fill(BLUE)
                text_rect = self.text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
                self.main_window.background.blit(
                    self.text,
                    text_rect
                )
            else:
                self.draw_objects()
                self.win_lose()
            
            self.update_window()

if __name__ == "__main__":
    Game().game_loop()