from Window import*
from Sprite import*
from Player import*
from constants import*
from functions import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BACKGROUND_IMAGE_PATH)

player = Player(PLAYER_WIDTH, PLAYER_HEIGHT, WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80, PLAYER_IMAGE_PATH, PLAYER_SPEED)
enemies = create_enemies()
bullets = pygame.sprite.Group()

game = True
finish = False
text = ""

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.fire(bullets)

    if not finish:
        window.screen.blit(window.bg_image, (0, 0))
        window.screen.blit(player.image, (player.rect.x, player.rect.y))

        enemies.draw(window.screen)
        bullets.draw(window.screen)

        enemies.update()
        bullets.update()

        player.control(pygame.K_a, pygame.K_d)

        finish, text = win(finish, text)
        finish, text = lose(finish, text)

    else:
        window.screen.blit(window.bg_image, (0, 0))
        window.screen.blit(text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    pygame.display.update()
    window.clock.tick(FPS)

