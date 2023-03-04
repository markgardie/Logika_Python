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

def win_lose(start_time, end_time, finish, text):

    font = pygame.font.Font(None, 50)

    if scores[0] > 5:
        text = font.render("Ти переміг", True, TEXT_COLOR)
        finish = True

    if end_time - start_time > 10:
        text = font.render("Ти програв", True, TEXT_COLOR)
        finish = True

    return finish, text
