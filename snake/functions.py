from constants import*
import pygame

def win_lose(snake):


    font = pygame.font.Font(None, 50)
    finish = False
    text = ""

    if scores[0] >= WIN_SCORE:
        finish = True
        text = font.render(WIN_TEXT, True, BLACK)

    if snake.hitbox.y < 5:
        finish = True
        text = font.render(LOSE_TEXT, True, BLACK)

    if snake.hitbox.y > WINDOW_HEIGHT - 5:
        finish = True
        text = font.render(LOSE_TEXT, True, BLACK)

    if snake.hitbox.x < 5:
        finish = True
        text = font.render(LOSE_TEXT, True, BLACK)

    if snake.hitbox.x > WINDOW_WIDTH - 5:
        finish = True
        text = font.render(LOSE_TEXT, True, BLACK)

    return finish, text