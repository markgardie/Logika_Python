from constants import*
from classes.Window import*
from classes.Card import*
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
            
    scores_text = SCORES_FONT.render(f"{SCORES_TEXT} {scores[0]}", True, TEXT_COLOR)
    window.screen.blit(scores_text, SCORES_TEXT_COR)

    pygame.display.flip()

    window.clock.tick(FPS)