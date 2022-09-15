import pygame
from constants import*
from konoval import*
from ivantsiv import*
from klimova import*

def drawWorm():
 for coord in wormCoords:
  x = coord["x"] * CELL_SIZE
  y = coord["y"] * CELL_SIZE
  worm_rect = pygame.Rect(x , y , CELL_SIZE , CELL_SIZE)
  pygame.draw.rect(WINDOW, DARK_GREEN , worm_rect)
  cell_rect = pygame.Rect(x + 4 , y + 4 , CELL_SIZE - 8 , CELL_SIZE - 8)
  pygame.draw.rect(WINDOW, GREEN , cell_rect)


def newCoords():
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


def drawing():
 WINDOW.fill(BG_COLOR)
 drawGrid()
 drawWorm(wormCoords)
 drawApple(apple)
 drawScore(len(wormCoords) - 3)
 pygame.display.update()
 FPS_CLOCK.tick(FPS)