import pygame as pg
import constants as const
from ball import Ball
from player import Player
from label import Label
from sprite import Sprite

class Game:

    #dz: player, score_label, ball, window, clock, scene, score, blocks
    def __init__(self):
        self.blocks = self.create_blocks()

    def create_blocks(self):
        blocks = []
        for i in range(15):
            row = i // 5
            col = i % 5

            block = Sprite(
                (50 + col*80, 20 + row*40),
                (const.BLOCK_WIDTH, const.BLOCK_HEIGHT),
                0,
                BLOCK_IMAGE_PATH1
            )

            blocks.append(block)

        return blocks
    
    #dz
    def update(self):
        pass

    #dz
    def draw(self):
        pass

    def win_lose(self):
        pass

    def collisions(self):
        pass

    def game_loop(self):
        pass
