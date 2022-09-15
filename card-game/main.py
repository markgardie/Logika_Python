import pygame
import os
from constants import*
from card import*
from card_builder import*
from click_fun import*

pygame.init()


#------Window

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Card Game")


fps = pygame.time.Clock()

#------Builders, cards
enemy_builder = CardBuilder(1)
big_builder = CardBuilder(4)
small_builder = CardBuilder(4, 10)

big_cards = big_builder.get_list()
small_cards = small_builder.get_list()
enemy_card = enemy_builder.get_list()

#------Game Cycle
game = True
clicked_card_num = 0

while game:

 for card in big_cards:
  window.blit(card.image, (card.x, card.y))

 for event in pygame.event.get():
  if event.type == pygame.QUIT:
game = False
  if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
clicked_card_num = on_card_click(big_cards, event)

 
 pygame.display.flip()
 window.fill(LEMON)
 fps.tick(60)
