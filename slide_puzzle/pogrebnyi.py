import pygame
import sys

pygame.init()

def terminate():
 pygame.quit()
 sys.exit()


def getLeftTopOfTile(tileX, tileY):
 left = XMARGIN + (tileX * TILESIZE) + (tileX - 1)
 top = YMARGIN + (tileY * TILESIZE) + (tileY - 1)
 return (left, top)


def drawBoard(board, message):
 window.fill(BGCOLOR)
 
 if message:
  textSurf, textRect = makeText(message, MESSAGECOLOR, BGCOLOR, 5, 5)
  window.blit(textSurf, textRect)

 for tilex in range(len(board)):
  for tiley in range(len(board[0])):
if board[tilex][tiley]:
 drawTile(tilex, tiley, board[tilex][tiley])


def resetAnimation(board, allMoves):
 # make all of the moves in allMoves in reverse.
 revAllMoves = allMoves[:] # gets a copy of the list
 revAllMoves.reverse()

 for move in revAllMoves: 
  if move == UP:
oppositeMove = DOWN
  elif move == DOWN:
oppositeMove = UP
  elif move == RIGHT:
oppositeMove = LEFT
  elif move == LEFT:
oppositeMove = RIGHT
  slideAnimation(board, oppositeMove, '', animationSpeed=int(TILESIZE / 2))
  makeMove(board, oppositeMove)
