from classes.Card import*
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

            pygame.draw.rect(window, card.color, card.hitbox)
            pygame.draw.rect(window, BLUE, card.hitbox, OUTLINE_THICKNESS)

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
            pygame.draw.rect(window, card.color, card.hitbox)
    
    return scores

def win_lose(start_time, end_time, finish, text):

    font = pygame.font.Font(FINAL_TEXT_FONT, FINAL_TEXT_SIZE)

    if end_time - start_time >= 11:
        text = font.render(LOSE_TEXT, True, TEXT_COLOR)
        finish = True

    if scores[0] > 5:
        text = font.render(WIN_TEXT, True, TEXT_COLOR)
        finish = True

    return finish, text

    


        

    
       
            
