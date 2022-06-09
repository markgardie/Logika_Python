import pygame
import os
from constants import*
from card import*
from card_builder import*

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

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            
    
    pygame.display.flip()
    window.fill(LEMON)
    fps.tick(60)
