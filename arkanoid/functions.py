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

def handle_collisions(blocks, platform, ball, direction_y, direction_x):
    
    #collide platform
    if ball.hitbox.colliderect(platform.hitbox):
        direction_y = -1

    #collide blocks
    for block in blocks:
        if ball.hitbox.colliderect(block.hitbox):
            blocks.remove(block)
            direction_y = 1 

    #collide left border
    if ball.x < 5: 
        direction_x = 1

    #collide right border
    if ball.x > 875:
        direction_x = -1

    #collide top border 
    if ball.y < 0:
        direction_y = 1

    
    return direction_y, direction_x