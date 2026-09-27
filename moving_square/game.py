import pygame
from constants import*
from player import Player

class Game:

    def __init__(self):
        self.player = Player()
        self.win_rect = pygame.Rect()
        self.lose_rect = pygame.Rect()

    def update(self):
        pass

    def draw(self):
        pass

    def win_lose(self):
        pass

    def loop(self):
        pass