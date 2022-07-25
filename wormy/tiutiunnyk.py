
import pygame
from constants import*
pygame.init()

#Window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Wormy")

#Clock
fps = pygame.time.Clock()


def show_start_screen(window):
    font = pygame.font.Font("freesansbold.ttf", 18)
    

    #GAME CYCLE
    game = True

    while game:

        #text1
        text1 = font.render("Wormy!", True, WHITE, DARKGRAY)
        degrees_1 = 0
        text1_rotate = pygame.transform.rotate(text1, degrees_1)
        rect1_rotate = text1_rotate.get_rect()
        rect1_rotate.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        window.blit(text1_rotate, rect1_rotate)

        #text2
        text2 = font.render("Wormy!", True, GREEN)
        degrees_2 = 0
        text2_rotate = pygame.transform.rotate(text2, degrees_2)
        rect2_rotate = text2_rotate.get_rect()
        rect2_rotate.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        window.blit(text2_rotate, rect2_rotate)
        


        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                game = False

        pygame.display.flip()
        window.fill(BG_COLOR)
        fps.tick(FPS)
        
        degrees_1 += 5
        degrees_2 += 10

#show_start_screen(window)


def showGameOverScreen():

    font = pygame.font.Font('freesansbold.ttf', 150)

    #Game
    game_text = font.render('Game', True, WHITE)
    gameRect = game_text.get_rect()
    gameRect.midtop = (WINDOW_WIDTH / 2, 10)
    window.blit(game_text, gameRect)
    #Over
    over_text = font.render('Over', True, WHITE)
    overRect = over_text.get_rect()
    overRect.midtop = (WINDOW_WIDTH / 2, gameRect.height + 10 + 25)
    window.blit(over_text, overRect)
    
    #draw_press_key_msg()

    pygame.display.update()
    
    #check_for_key_press()
    