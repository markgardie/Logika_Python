from curses import window
from math import degrees
from constants import*

def show_start_screen(window): 
    font = pygame.font.Font("freesansbold.ttf ", 100)
    text1 = font.render("Wormy!", True, WHITE, DARKGREEN)
    text2 =  font.render("Wormy!", True, GREEN)

    degrees1 = 0
    degrees2 = 0
    while True:
        window.fill(BG_COLOR)
        rotated_surf1 = pygame.transform.rotate(text1, degrees1)
        rotated_rect1 = rotated_surf1.get_rect()
        rotated_rect1.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        window.blit(rotated_surf1,rotated_rect1 )
        
        rotated_surf2 = pygame.transform.rotate(text1, degrees1)
        rotated_rect2 = rotated_surf2.get_rect()
        rotated_rect2.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        window.blit(rotated_surf1,rotated_rect2 )

        drow_press_key_msg()

        if check_for_key_press():
            pygame.event.get()
            return 
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3
        degrees2 += 7


def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)



def draw_apple(apple_coords, window):
    for coord in worm_coords:
        x = coord["x"] * CELL_SIZE
        y = coord["y"] * CELL_SIZE
        apple_rect = pygame.Rect(x , y , CELL_SIZE , CELL_SIZE)
        pygame.draw.rect(window, RED, apple_rect)
        

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key




 