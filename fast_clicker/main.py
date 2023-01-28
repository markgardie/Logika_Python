from constants import*
from Window import*
from Card import*
from functions import create_cards, draw_cards, click

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BACKGROUND_COLOR)
cards = create_cards(window.screen)


game = True

while game:
    draw_cards(window.screen, cards)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            click(window.screen, cards, e)


    
    pygame.display.flip()

    window.clock.tick(FPS)