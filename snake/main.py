from constants import*
from functions import*
from Window import*
from Sprite import*
from Snake import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE)

snake = Snake(SNAKE_WIDTH, SNAKE_HEIGHT, SNAKE_X, SNAKE_Y, SNAKE_IMAGE, SNAKE_SPEED)

font = pygame.font.Font(None, 40)
game = True
finish = False
text = ""

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if not finish:
        counter_text = font.render(f"Бали: {scores[0]}")

        window.screen.blit(snake.image, (snake.hitbox.x, snake.hitbox.y))
        window.screen.blit(counter_text, (100, 100))
        
        snake.move()
        snake.controls(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)

    else:
        window.screen.blit(text, (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2 - 50))

    pygame.display.flip()
    window.screen.fill(BLUE)
    window.clock.tick(FPS)
    