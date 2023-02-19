import pygame as pg
from constants import*
from Card import*
from random import randint

wait = 0
click_text = 0

def create_cards(cards_num):
    cards = []

    x = START_X

    for i in range(cards_num):
        card = Card(x, CARDS_Y, YELLOW, CARD_WIDTH, CARD_HEIGHT)
        cards.append(card)
        x += CARDS_DISTANCE

    return cards

def draw_cards(window, cards):

    global wait

    if wait == 0:

        wait = 30
        global click_text
        click_text = randint(0, len(cards) - 1)

        for card in cards:
            card.color = YELLOW

            pg.draw.rect(window, card.color, card.rect)
            pg.draw.rect(window, BLUE, card.rect, OUTLINE_THICKNESS)

            if cards.index(card) == click_text:
                pass

    else:
        wait -= 1