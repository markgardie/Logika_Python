import click
import pygame
import os
from constants import*
from card import*
from card_builder import*
from draw_cards import*
from click_fun import*

pygame.init()


#------Window

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Card Game")


fps = pygame.time.Clock()

#------Builders, cards
enemy_builder = EnemyCardBuilder()
big_builder = CardBuilder(4)
small_builder = CardBuilder(4, 10)

big_cards = big_builder.get_list()
small_cards = small_builder.get_list()
enemy_card = enemy_builder.get_enemy()

#------Game Cycle
game = True
flag = 0
clicked_card_num = 0

while game:

    draw_enemy_card(enemy_card, window)
    flag = draw_big_cards(flag, big_cards, window, clicked_card_num)
    draw_small_cards(flag, small_cards, window, clicked_card_num)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked_card_num = onclick_card(big_cards ,event)
            flag = 10
            
    pygame.display.flip()
    window.fill(LEMON)
    fps.tick(60)
