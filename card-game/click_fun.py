

def onclick_card(cards, event):

    x, y = event.pos

    for card in cards:
        if card.rect.collidepoint(x, y):
            for el in cards:
                el.key_pressed = True
            print(f"Card {card.num} has been clicked")
            card.key_pressed = True
            return card.num