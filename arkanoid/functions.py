from Sprite import*
from constants import*

def create_blocks():
    blocks = []

    x = 20
    y = 20

    for row in MAP:
        for place in row:
            if place == "1":
                block = Sprite(BLOCK_WIDTH, BLOCK_HEIGHT, x, y, BLOCK_IMAGE_PATH)
                blocks.append(block)
            x += 76
        y += 56
        x = 20

    return blocks


def draw_blocks(blocks, window):

    for block in blocks:
        window.blit(block.image, (block.hitbox.x, block.hitbox.y))


def collisions(ball, platform, blocks, direction_x, direction_y):

    if ball.hitbox.x < 5:
        direction_x = 1