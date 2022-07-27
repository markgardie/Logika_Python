import pygame
from constants import*

def make_text(text, text_color, bg_color, top, left):
    font = pygame.font.Font("freesansbold.ttf", FONT_SIZE)
    final_text = font.render(text, True, text_color, bg_color)
    final_text_rect = final_text.get_rect()
    final_text_rect.topLeft = (top, left)
    return text, text.rect


def getStartingBoard():
    counter = 1
    board = []
    for x in range (BOARD_WIDTH):
        column = []
        for y in range(BOARD_HEIGHT):
            column.append(counter)
            counter += BOARD_WIDTH
        board.append(column)
        counter -= BOARD_WIDTH*(BOARD_HEIGHT-1)+BOARD_WIDTH-1
    board[BOARD_WIDTH-1][BOARD_HEIGHT-1] = None
    return board

def SlideAnimation(board, direction, message, animationSpeed):
    blanx, blanky = getBlankPosition(board)
    if direction == UP:
        movex = blankx
        movey = blanky + 1
    if direction == DOWN:
        movex = blankx
        movey = blanky - 1
    if direction == RIGHT:
        movex = blankx
        movey = blanky + 1
    if direction == LEFT:
        movex = blankx
        movey = blanky - 1

    drawBoard[board, message]
    basesurf = DISPLAYSURF.copy()

    moveleft, movetop = getLeftTopOfTile(movex, movey)
    pygame.draw.rect(baseSurf, BGCOLOR, (moveLeft, moveTop, TILESIZE, TILESIZE))

    for i in range(0, TILESIZE, animationSpeed):
        checkForQuit()
        DISPLAYSURF.blit(baseSurf, (0, 0))
        if direction == UP:
            drawTile(movex, movey, board[movex][movey], 0, -i)
        if direction == DOWN:
            drawTile(movex, movey, board[movex][movey], 0, i)
        if direction == RIGHT:
            drawTile(movex, movey, board[movex][movey], -i, 0)
        if direction == LEFT:
            drawTile(movex, movey, board[movex][movey], i, 0)

    pygame.display.update()
    FPSCLLOCK.tick(FPS)