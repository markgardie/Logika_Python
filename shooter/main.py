from Window import*
from Sprite import*
from Player import*
from constants import*
from create_enemies import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BACKGROUND_IMAGE_PATH)

player = Player(PLAYER_WIDTH, PLAYER_HEIGHT, WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80, PLAYER_IMAGE_PATH, PLAYER_SPEED)
enemies = create_enemies()
bullets = pygame.sprite.Group()

game = True

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.fire(bullets)


    window.screen.blit(window.bg_image, (0, 0))
    window.screen.blit(player.image, (player.hitbox.x, player.hitbox.y))

    enemies.draw(window.screen)
    bullets.draw(window.screen)

    enemies.update()
    bullets.update()

    player.control(pygame.K_a, pygame.K_d)

    pygame.display.update()
    window.clock.tick(FPS)