from constants import*
from functions import*
from Window import*
from Sprite import*
from Snake import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE)

snake = Snake(SNAKE_WIDTH, SNAKE_HEIGHT, SNAKE_X, SNAKE_Y, SNAKE_IMAGE, SNAKE_SPEED)


game = True
finish = False
text = ""

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if not finish:

    else: