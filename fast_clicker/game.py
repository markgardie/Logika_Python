from constants import*
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
        self.score = 0
        self.start_time = time()
        self.goal_card = 0

        pg.font.init()

    def create_objects(self):
        self.main_window = Window(
            WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE
        )
        
        self.cards = self.create_cards()

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
        self.draw_cards()

    def draw_cards(self):
        if self.timer == 0:
            self.timer = 60
            self.goal_card = randint(0, len(self.cards) - 1)

            for card in self.cards:
                card.set_color(YELLOW)

                pg.draw.rect(self.main_window.background, card.color, card.hitbox)
                pg.draw.rect(self.main_window.background, BLUE, card.hitbox, OUTLINE_THICKNESS)

                if self.cards.index(card) == self.goal_card:
                    self.main_window.blit(card.text, 
                                          (card.hitbox.x + TEXT_X_SHIFT, 
                                           card.hitbox.y + TEXT_Y_SHIFT
                                           )
                                          )
        else:
            self.timer -= 1

    def collisions(self):
        self.click()

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
        font = pg.font.Font(FINAL_TEXT_FONT, FINAL_TEXT_SIZE)

        if self.end_time - self.start_time >= 11:
            self.text = font.render(LOSE_TEXT, True, TEXT_COLOR)
            self.finish = True
        
        if self.scores > 5: 
            self.text = font.render(WIN_TEXT, True, TEXT_COLOR)
            self.finish = True

    def update_window(self):
        self.main_window.clock.tick(60)
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
            self.update_window()
            if self.finish:
                self.main_window.background.blit(
                    self.text,
                    (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
                )
            else:
                self.draw_objects()
                self.collisions()
                self.win_lose()
                self.end_time = time()
                

Game().game_loop()