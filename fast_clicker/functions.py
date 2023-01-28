from Card import*
from constants import*
from random import randint

wait = 0
click_text = 0

def create_cards():
    cards = []
    x = START_X

    for i in range(CARDS_NUM):
        card = Card(x, CARDS_Y, CARD_WIDTH, CARD_HEIGHT, YELLOW, TEXT, TEXT_SIZE, DARK_BLUE, FONT)
        cards.append(card)
        x += CARDS_DISTANCE

    return cards