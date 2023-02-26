from Card import*
from Window import*
from constants import*
from functions import*


window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BACKGROUND_COLOR)

cards = create_cards(window)

game = True
finish = False

while game:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    pygame.display.flip()
    window.clock.tick(FPS)