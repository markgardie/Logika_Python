from Card import*
from constants import*
from random import randint

wait = 0
click_text = 0

def create_cards(window):
    cards = []

    x = START_X
    
    for i in range(CARDS_NUM):
    
        new_card = Card(x, CARDS_Y, CARD_WIDTH, CARD_HEIGHT, YELLOW, TEXT, TEXT_SIZE, TEXT_COLOR, FONT)
       

        cards.append(new_card)
        x += CARDS_DISTANCE
    
    return cards

def draw_cards(window, cards):

    global wait

    if wait == 0:

        wait = 60
        global click_text

        click_text = randint(1, len(cards))

        for card in cards:
            card.set_color(YELLOW)

            pg.draw.rect(window, card.color, card.hitbox)
            pg.draw.rect(window, BLUE, card.hitbox, OUTLINE_THICKNESS)

            if (cards.index(card) + 1) == click_text:
                window.blit(card.text, (card.hitbox.x + TEXT_X_SHIFT, card.hitbox.y + TEXT_Y_SHIFT))
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
            pg.draw.rect(window, card.color, card.hitbox)

def win_lose():
    if scores[0] == 5:

      