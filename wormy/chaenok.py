import pygame
from constants import*
pygame.init()

def draw_worm(worm_coords, window):
    for coord in worm_coords:
        x = coord["x"] * CELL_SIZE
        y = coord["y"] * CELL_SIZE
        worm_rect = pygame.Rect(x , y , CELL_SIZE , CELL_SIZE)
        pygame.draw.rect(window, DARK_GREEN , worm_rect)
        cell_rect = pygame.Rect(x + 4 , y + 4 , CELL_SIZE - 8 , CELL_SIZE - 8)
        pygame.draw.rect(window, GREEN , cell_rect)


def newCoords(wormCoords, direction):
     # move the worm by adding a segment in the direction it is moving
    if direction == UP:
        newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
    elif direction == DOWN:
        newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
    elif direction == LEFT:
        newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
    elif direction == RIGHT:
        newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
    
    wormCoords.insert(0, newHead)


def drawing(window, wormCoords, apple):
    window.fill(BGCOLOR)
    drawGrid()
    drawWorm(wormCoords)
    drawApple(apple)
    drawScore(len(wormCoords) - 3)
    pygame.display.update()
    FPSCLOCK.tick(FPS)