import pygame

def check_for_quit():
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
terminate()


def  handleClicks(): 
 for event in pygame.event.get(): # event handling loop 
if event.type == MOUSEBUTTONUP: 
 spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1]) 
 
 if (spotx, spoty) == (None, None): 
  # check if the user clicked on an option button 
  if RESET_RECT.collidepoint(event.pos): 
resetAnimation(mainBoard, allMoves) # clicked on Reset button 
allMoves = [] 
  elif NEW_RECT.collidepoint(event.pos): 
mainBoard, solutionSeq = generateNewPuzzle(80) # clicked on New Game button 
allMoves = [] 
  elif SOLVE_RECT.collidepoint(event.pos): 
resetAnimation(mainBoard, solutionSeq + allMoves) # clicked on Solve button 
allMoves = [] 
 else: 
  # check if the clicked tile was next to the blank spot 
 
  blankx, blanky = getBlankPosition(mainBoard) 
  if spotx == blankx + 1 and spoty == blanky: 
slideTo = LEFT 
  elif spotx == blankx - 1 and spoty == blanky: 
slideTo = RIGHT 
  elif spotx == blankx and spoty == blanky + 1: 
slideTo = UP 
  elif spotx == blankx and spoty == blanky - 1: 
slideTo = DOWN


def handleKeys():
 for event in pygame.event.get():
  if event.type == KEYUP:
# check if the user pressed a key to slide a tile
if event.key in (K_LEFT, K_a) and isValidMove(mainBoard, LEFT):
 slideTo = LEFT
elif event.key in (K_RIGHT, K_d) and isValidMove(mainBoard, RIGHT):
 slideTo = RIGHT
elif event.key in (K_UP, K_w) and isValidMove(mainBoard, UP):
 slideTo = UP
elif event.key in (K_DOWN, K_s) and isValidMove(mainBoard, DOWN):
 slideTo = DOWN

def moveTile(slideTo):
 if slideTo:
  slideAnimation(mainBoard, slideTo, 'Click tile or press arrow keys to slide.', 8) # show slide on screen
  makeMove(mainBoard, slideTo)
  allMoves.append(slideTo) # record the slide
