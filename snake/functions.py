from constants import*
import pygame
from Snake import*

# зіткнення з їжею
def food_collision(snake, food):

    # в зіткненнях завжди приймають участь хітбокси
    # якщо змійка торкнулась їжі
    if snake.hitbox.colliderect(food.hitbox):
        # то їжу перемущуємо у випадкову точку
        food.move()
        # збільшуємо кількість балів
        scores[0] += 1

# перевірка перемоги та поразки
def win_lose(snake):

    # змінна, яка зберігає шрифт для роботи з текстом
    # шрифт стандартний, розмір 50
    font = pygame.font.Font(None, 50)
    # змінна, яка відповідає за переключення на фінальний екран
    finish = False
    # текст на фінальному екрані
    text = ""

    # якщо ми отримали необхіднку кількість балів
    if scores[0] >= WIN_SCORE:
        # перемикаємось на фінальний екран
        finish = True
        # створюємо переможний текст
        text = font.render(WIN_TEXT, True, BLACK)

    # якщо змійка торкається верхньої межі
    if snake.hitbox.y < 5:
        # перемикаємось на фінальний екран
        finish = True
        # створюємо текст поразки
        text = font.render(LOSE_TEXT, True, BLACK)
    
    # якщо змійка торкається нижньої межі
    if snake.hitbox.y > WINDOW_HEIGHT - 5:
        # перемикаємось на фінальний екран
        finish = True
        # створюємо текст поразки
        text = font.render(LOSE_TEXT, True, BLACK)
    
    # якщо змійка торкається лівої межі
    if snake.hitbox.x < 5:
        # перемикаємось на фінальний екран
        finish = True
        # створюємо текст поразки
        text = font.render(LOSE_TEXT, True, BLACK)
    
    # якщо змійка торкається правої межі
    if snake.hitbox.x > WINDOW_WIDTH - 5:
        # перемикаємось на фінальний екран
        finish = True
        # створюємо текст поразки
        text = font.render(LOSE_TEXT, True, BLACK)
    

    return finish, text