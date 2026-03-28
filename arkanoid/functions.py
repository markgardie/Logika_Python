
from constants import*
from Sprite import*

def create_blocks():

    blocks = []

    x = 20
    y = 20

    for row in MAP:
        for place in row:
            if place == "1":
                block = Sprite(BLOCK_WIDTH, BLOCK_HEIGHT, x, y, "block.png")
                blocks.append(block)
            x += 76
        y += 56
        x = 20

    return blocks
    
