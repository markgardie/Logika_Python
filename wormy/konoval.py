import pygame
from pygame.locals import*
import random
from constants import*
from ivantsiv import*
from chaenok import*


def drawPressKeyMsg(): 
    key_text = BASIC_FONT.render("Натисніть а, щоб роспочати гру", True,(250,0,250))
    key_text_rect = key_text.get_rect()
    key_text_rect.topleft = (WINDOW_WIDTH - 150, WINDOW_HEIGHT - 100)
    WINDOW.blit(key_text,key_text_rect)

def initialState():
    global wormCoords, direction, apple

    start_x = random.randint(5, CELL_WIDTH - 6 ) 
    start_y = random.randint(5, CELL_WIDTH - 6 ) 
    wormCoords = [{"x": start_x, "y": start_y}, 
                {"x": start_x-1, "y": start_y},
                {"x": start_x-2, "y": start_y}]
    direction = RIGHT 
    apple = getRandomLocation()

def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == K_RIGHT and direction != LEFT:
                direction = RIGHT
            elif event.key == K_UP and direction != DOWN:
                direction = UP
            elif event.key == K_DOWN and direction != UP:
                direction = DOWN
            elif event.key == pygame.K_ESCAPE:
                terminate()
            
def runGame():
    initialState()
    while True:
        handleEvents()
        handleLose()
        handleAppleTouch()
        newCoords()
        drawing()
