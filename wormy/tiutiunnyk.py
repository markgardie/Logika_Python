
import pygame
import random
from constants import*
from konoval import*
from klimova import*
from chaenok import*
from ivantsiv import*

def main():
    global FPS_CLOCK, WINDOW, BASIC_FONT

    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    BASIC_FONT = pygame.font.Font('freesansbold.ttf', 18)
    FPS_CLOCK = pygame.time.Clock()
    pygame.display.set_caption("Wormy")

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def showStartScreen():
  
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    text1 = titleFont.render('Wormy!', True, WHITE, DARK_GREEN)
    text2 = titleFont.render('Wormy!', True, GREEN)

    degrees1 = 0
    degrees2 = 0
    
    while True:

        WINDOW.blit(BG_COLOR)
        
        #text1
        text1_rotate = pygame.transform.rotate(text1, degrees1)
        rect1_rotate = text1_rotate.get_rect()
        rect1_rotate.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        WINDOW.blit(text1_rotate, rect1_rotate)

        #text2
        text2_rotate = pygame.transform.rotate(text2, degrees2)
        rect2_rotate = text2_rotate.get_rect()
        rect2_rotate.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        WINDOW.blit(text2_rotate, rect2_rotate)
        
        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        FPS_CLOCK.tick(FPS)
        degrees1 += 3 # rotate by 3 degrees each frame
        degrees2 += 7 # rotate by 7 degrees each frame

def showGameOverScreen():

    font = pygame.font.Font('freesansbold.ttf', 150)

    #Game
    game_text = font.render('Game', True, WHITE)
    gameRect = game_text.get_rect()
    gameRect.midtop = (WINDOW_WIDTH / 2, 10)
    WINDOW.blit(game_text, gameRect)
    #Over
    over_text = font.render('Over', True, WHITE)
    overRect = over_text.get_rect()
    overRect.midtop = (WINDOW_WIDTH / 2, gameRect.height + 10 + 25)
    WINDOW.blit(over_text, overRect)
    
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() 

    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return


