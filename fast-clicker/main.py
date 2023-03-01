from constants import*
from classes.Window import*
from classes.Card import*
from functions import create_cards, draw_cards, click, win_lose
from time import time


window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BACKGROUND_COLOR)
cards = create_cards(window.screen)

game = True
finish = False
text = ""

start_time = time()

while game:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            click(window.screen, cards, e)
            

    if not finish:
        draw_cards(window.screen, cards)
        end_time = time()
        finish, text = win_lose(start_time, end_time, finish, text)
    else:
        window.screen.fill(BACKGROUND_COLOR)
        window.screen.blit(text, (WINDOW_WIDTH / 2 - FINAL_TEXT_SIZE, WINDOW_HEIGHT / 2 - FINAL_TEXT_SIZE))

    pygame.display.flip()
    
    window.clock.tick(FPS)