from constants import*
from functions import*
from Window import*
from Sprite import*
from Snake import*
from Food import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE)

snake = Snake(SNAKE_WIDTH, SNAKE_HEIGHT, SNAKE_X, SNAKE_Y, GREEN, SNAKE_SPEED)
food = Food(FOOD_WIDTH, FOOD_HEIGHT, FOOD_X, FOOD_Y, RED, FOOD_SPEED)
tail = []

font = pygame.font.Font(None, 40)
game = True
finish = False
text = ""

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if not finish:
        counter_text = font.render(f"Бали: {scores[0]}", BLACK)

        pygame.draw.rect(window.screen, snake.color, snake.hitbox)
        pygame.draw.rect(window.screen, food.color, food.hitbox)
        window.screen.blit(counter_text, (100, 100))
        
        food_collision(snake, food)
        snake.move()
        snake.controls(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)

    else:
        window.screen.blit(text, (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2 - 50))

    pygame.display.flip()
    window.screen.fill(BLUE)
    window.clock.tick(FPS)
    