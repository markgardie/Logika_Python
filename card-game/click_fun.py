

def onclick_card(cards, event):

    x, y = event.pos

    for card in cards:
        if card.rect.collidepoint(x, y):
            print(f"Card {card.num} has been clicked")
            return card.num