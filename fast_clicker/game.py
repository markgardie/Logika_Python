from constants import*
from sprite import Sprite
from window import Window
from card import Card
from label import Label
from random import randint
import pygame as pg

class Game():

    def __init__(self):
        self.timer = 0
        self.score = 0
        self.start_time = time()
        self.goal_card = 0

    def create_objects(self):
        pg.font.init()
        pass

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
        pass

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

    def move_objects(self):
        pass

    def collisions(self):
        pass

    def win_lose(self):
        pass

    def update_window(self):
        self.main_window.clock.tick(60)
        pg.display.update()

    def event_handler(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.game = False

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
                self.move_objects()
                self.collisions()
                self.win_lose()
                

Game().game_loop()