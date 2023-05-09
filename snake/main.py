from constants import*
from functions import*
from Window import*
from Sprite import*
from Snake import*
from Food import*

# створюємо вікно
window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, BLUE, CAPTION)
# створюємо змійку
snake = Snake(SNAKE_WIDTH, SNAKE_HEIGHT, SNAKE_X, SNAKE_Y, GREEN, SNAKE_SPEED)
# створюємо їжу
food = Food(FOOD_WIDTH, FOOD_HEIGHT, FOOD_X, FOOD_Y, RED, FOOD_SPEED)

# змінна, яка зберігає шрифт для роботи з текстом
# шрифт стандартний, розмір 40
font = pygame.font.Font(None, 40)
# змінна, яка відповідає за запуск та закриття гри
game = True
# змінна, яка відповідає за переключення на фінальний екран
finish = False
# текст на фінальному екрані
text = ""

# ігровий цикл
while game:
    # перевірка подій
    for event in pygame.event.get():
        # перевіряємо натискання на крестик вікна
        if event.type == pygame.QUIT:
            # якщо натиснуто, то закриваємо вікно
            game = False

    # якщо ще НЕ фінальний екран
    if not finish:
        # створюємо текст лічильника балів
        counter_text = font.render(f"Бали: {scores[0]}", True, BLACK)

        # малюємо прямокутник змійки
        pygame.draw.rect(window.screen, snake.color, snake.hitbox)
        # малюємо прямокутник їжі
        pygame.draw.rect(window.screen, food.color, food.hitbox)
        # малюємо текст лічильника
        window.screen.blit(counter_text, (100, 100))
        
        # запускаємо керування змійкою
        snake.controls(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
        # запускаємо автоматичний рух змійки
        snake.move()

        # перевіряємо зіткнення змійки та їжі
        food_collision(snake, food)
        # перевіряємо перемогу та поразку
        finish, text = win_lose(snake)
    # якщо вже є перемикання на фінальний екран
    else:
        # малюємо на фінальному екрані тільки текст
        window.screen.blit(text, (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2 - 50))

    # оновлення екрану
    pygame.display.flip()
    # заливка фону
    window.screen.fill(BLUE)
    # тіки годинника
    window.clock.tick(FPS)
