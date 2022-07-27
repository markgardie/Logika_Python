import pygame  #Імпортував пай гейм 
 
#------ Перевіряє кліки на плитку та на меню                     
def getSpotClicked(board, x, y): 
    for tileX in range(len(board)): 
        for tileY in range(len(board[0])): 
            left, top = getLeftTopOfTile(tileX, tileY) 
            tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE) 
            if tileRect.collidepoint(x, y): 
                return (tileX, tileY) 
    return (None, None) 
 
#---друга функція!-----З пересування плики на пусту 
 
def isValidMove(board, move): 
    blankx, blanky = getBlankPosition(board) 
    return (move == UP and blanky != len(board[0]) - 1) or \ 
           (move == DOWN and blanky != 0) or \ 
           (move == LEFT and blankx != len(board) - 1) or \ 
           (move == RIGHT and blankx != 0) 
 
def getBlankPosition(board): 
    # Return the x and y of board coordinates of the blank space. 
    for x in range(BOARDWIDTH): 
        for y in range(BOARDHEIGHT): 
            if board[x][y] == BLANK: 
                return (x, y) 
 
 
def makeMove(board, move): 
    # This function does not check if the move is valid. 
    blankx, blanky = getBlankPosition(board) 
 
    if move == UP: 
        board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky] 
    elif move == DOWN: 
        board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky] 
    elif move == LEFT: 
        board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky] 
    elif move == RIGHT: 
        board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]                                                 
 
 
def initialState (): 
    RESET_SURF, RESET_RECT = makeText('Reset',    TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 90) 
    NEW_SURF,   NEW_RECT   = makeText('New Game', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 60) 
    SOLVE_SURF, SOLVE_RECT = makeText('Solve',    TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 30) 
 
    mainBoard, solutionSeq = generateNewPuzzle(80) 
    SOLVEDBOARD = getStartingBoard() # a solved board is the same as the board in a start state. 
    allMoves = [] # list of moves made from the solved configuration 
 
 
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