import pygame
import sys
pygame.init()



def terminate():
    pygame.quit() 
    sys.exit()

def getRandomLocation():
    return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}

def drawGrid():

    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(window, DARK_GRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(window, DARK_GRAY, (0, y), (WINDOW_WIDTH, 0))


def handleLose(wormCoords):
    
    if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
        return # game over

    for wormBody in wormCoords[1:]:
        if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
            return # game over

def handleAppleTouch(wormCoords):
    # check if worm has eaten an apply
    if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            # don't remove worm's tail segment
        apple = getRandomLocation() # set a new apple somewhere
    else:
        del wormCoords[-1] # remove worm's tail segment

