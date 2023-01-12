from classes.Card import*
from constants import*

def create_cards(window):
    cards = []

    x = START_X
    
    for i in range(CARDS_NUM):
    
        new_card = Card(x, CARDS_Y, CARD_WIDTH, CARD_HEIGHT, YELLOW, TEXT, TEXT_SIZE, TEXT_COLOR, FONT)
       

        cards.append(new_card)
        x += CARDS_DISTANCE
    
    return cards

def draw_cards(window, cards):

    for card in cards:
        pygame.draw.rect(window, card.color, card.hitbox)
        pygame.draw.rect(window, BLUE, card.hitbox, OUTLINE_THICKNESS)
        window.blit(card.text, (card.hitbox.x + TEXT_X_SHIFT, card.hitbox.y + TEXT_Y_SHIFT))
            
