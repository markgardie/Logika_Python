import pygame as pg
from constants import*
from Card import*
from random import randint
from time import time

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
                window.blit(card.text, (card.rect.x + TEXT_X_SHIFT, card.rect.y + TEXT_Y_SHIFT))

    else:
        wait -= 1

def click(window, cards, e):
    x, y = e.pos
    for card in cards:
        if card.collide(x, y):
            if (cards.index(card) + 1) == click_text:
                card.set_color(GREEN)
                scores[0] += 1
            else:
                card.set_color(RED) 
                scores[0] -= 1
            pygame.draw.rect(window, card.color, card.hitbox)
    
def win_lose(window, finish):

    if scores[0] == 5:
        win_text = pygame.font.Font(None, FINISH_TEXT_SIZE).render(WIN_TEXT, True, FINISH_TEXT_COLOR)
        finish = True