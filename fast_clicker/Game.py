from Window import Window
from Sprite import Sprite
from Label import Label
from Card import Card
from Constants import*
import pygame as pg
from random import randint

class Game():

    def create_objects(self):

        self.window = Window(
            WINDOW_WIDTH, WINDOW_HEIGHT,
            CAPTION, BLUE
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

        card_num = randint(0, len(self.cards) - 1)

        for card in self.cards:
            pg.draw.rect(self.window.screen, card.color, card.hitbox)


    def move_objects(self):

        pass

    def collisions(self):
        
       self.click()

    def click(self, e):
        x, y = e.pos
        for card in self.cards:
            if card.hitbox.collidepoint(x, y):
                pass``

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