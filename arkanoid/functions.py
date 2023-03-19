from Sprite import*
from constants import*
from random import randint

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


def collisions(ball, platform, blocks):

    # м'яч і платорфми
    if ball.hitbox.colliderect(platform.hitbox):
        direction_y = -1
        direction_x = randint(-1, 1)

    # м'яч і блоки
    for block in blocks:
        if ball.hitbox.colliderect(block.hitbox):
            direction_y = 1
            direction_x = randint(-1, 1)

    # м'яч і ліва межа
    if ball.hitbox.x < 5:
        direction_x = 1

    # м'яч і права межа
    if ball.hitbox.x > WINDOW_WIDTH - 5:
        direction_x = -1

    # м'яч і верхня межа
    if ball.hitbox.y < 5:
        direction_y = 1
        direction_x = randint(-1, 1)


    return direction_x, direction_y

def win(blocks):
    if len(blocks) == 0:
        finish = True

        font = pygame.font.Font(None, 50)

        text = font.render("Ти переміг", True, BLACK)

        return finish, text
    
def lose(ball):
    if ball.hitbox.y > WINDOW_HEIGHT - 5:
        finish = True

        font = pygame.font.Font(None, 50)

        text = font.render("Ти програв", True, BLACK)

        return finish, text
