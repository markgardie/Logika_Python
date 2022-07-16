
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

show_start_screen(window)