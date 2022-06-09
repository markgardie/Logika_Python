

def draw_big_cards(flag, cards, window, clicked_card_num):
    
    if flag == 0:
        for card in cards:
            window.blit(card.image, (card.x, card.y))
    else:
        flag -= 1
        for card in cards:
            if card.num != clicked_card_num:
                window.blit(card.image, (card.x, card.y))

    return flag


def draw_small_cards(flag, cards, window, clicked_card_num):

    if flag > 0:
        for card in cards:
            if card.num == clicked_card_num:
                window.blit(card.image, (card.x, card.y))


def draw_enemy_card(enemy, window):
    window.blit(enemy.image, (enemy.x, enemy.y))