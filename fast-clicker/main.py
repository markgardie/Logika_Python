from constants import*
from classes.Window import*
from classes.Card import*
from functions import create_cards, draw_cards

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BACKGROUND_COLOR)
cards = create_cards(window.screen)


game = True

while game:
    draw_cards(window.screen, cards)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    
    pygame.display.flip()

    window.clock.tick(FPS)