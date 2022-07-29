import pygame
import sys
import random
from constants import*
from konoval import*



def terminate():
    pygame.quit() 
    sys.exit()

def getRandomLocation():
    return {'x': random.randint(0, CELL_WIDTH - 1), 'y': random.randint(0, CELL_HEIGHT - 1)}

def drawGrid():

    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(WINDOW, DARK_GRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(WINDOW, DARK_GRAY, (0, y), (WINDOW_WIDTH, 0))


def handleLose():
    
    if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELL_WIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
        return # game over

    for wormBody in wormCoords[1:]:
        if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
            return # game over

def handleAppleTouch():
    # check if worm has eaten an apply
    if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            # don't remove worm's tail segment
        apple = getRandomLocation() # set a new apple somewhere
    else:
        del wormCoords[-1] # remove worm's tail segment

