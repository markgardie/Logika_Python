
def on_card_click(cards, event):
 x, y = event.pos

 for card in cards:
  if card.rect.collidepoint(x,y):
print(f"Карточка номер {card.card_num} була натиснута")
return card.card_num