from constants import*
from sprite import*

def create_blocks(blocks):
    x = 20 
    y = 20 

    for raw in MAP:
        for place in raw:
            if place == "1":
                block = Sprite(BLOCK_WIDTH, BLOCK_HEIGHT, x, y, "block.png")
                block.load_image()
                blocks.append(block)
            x += 76
        y += 56
        x = 20

def draw_blocks(blocks, window):

    for block in blocks:
        window.blit(block.image, (block.x, block.y))