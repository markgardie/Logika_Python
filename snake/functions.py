from constants import*
import pygame
from Snake import*

def food_collision(snake, food):

    if snake.hitbox.colliderect(food.hitbox):
        food.move()
        scores[0] += 1

        snake.hitbox.width += SNAKE_WIDTH

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