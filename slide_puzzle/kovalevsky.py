from constants import*
import pygame

def main():
 pygame.init()

 window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
 pygame.display.set_caption("Slide Puzzle")


 fps = pygame.time.Clock()
 pygame.display.flip()
 window.fill(BLACK)
 fps.tick(60)


 game = True

 while game:

  for event in pygame.event.get():

if event.type == pygame.QUIT:
 game = False

  pygame.display.flip()
  window.fill(BLACK)
  fps.tick(60)


def getRandomMove(board,lastMove = None):
 validMoves = [UP,DOWN,LEFT,RIGHT]
 if lastMove == UP or not isValidMove(board, DOWN):
  validMoves.remove(DOWN)
 if lastMove == DOWN or not isValidMove(board, UP):
  validMoves.remove(UP)
 if lastMove == RIGHT or not isValidMove(board, LEFT):
  validMoves.remove(LEFT)
 if lastMove == LEFT or not isValidMove(board, RIGHT):
  validMoves.remove(RIGHT)
 random.choice(validMoves)


def drawTile(tilex, tiley, number, adjx = 0, adjy = 0):

 left, top = getLeftTopOfTile(tilex, tiley)
 pygame.draw.rect(window, TILE_COLOR, left + adjx, top + adjy, TILE_SIZE, TILE_SIZE)

 font = pygame.font.Font("freesansbold.ttf", FONT_SIZE)

 textSurf = font.render(str(number), True, TEXT_COLOR)
 textRect = textSurf.get_rect()
 textRect.center = left + int(TILE_SIZE / 2) + adjx, top + int(TILE_SIZE / 2) + adjy
 window.blit(textSurf, textRect) 
