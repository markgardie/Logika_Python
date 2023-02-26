from constants import*
from Card import*
from Window import*
from functions import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BACKGROUND_COLOR)

cards = create_cards(CARDS_NUM)

game = True

while game:

    draw_cards(window.screen, cards)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            click(window, cards, e)


    pygame.display.flip()
    window.clock.tick(FPS)