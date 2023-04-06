from constants import*
from functions import*
from Window import*
from Sprite import*
from Player import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, BLUE, CAPTION)

player = Player(PLAYER_WIDTH, 
                PLAYER_HEIGHT, 
                PLATFORM1_X + PLATFORM_WIDTH / 2 - PLAYER_WIDTH, 
                PLATFORM1_Y - PLAYER_HEIGHT, 
                PLAYER_IMAGE_PATH, 
                PLAYER_SPEED)

platform1 = Sprite(PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM1_X, PLATFORM1_Y, PLATFORM_IMAGE_PATH, PLATFORM_SPEED)
platform2 = Sprite(PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM2_X, PLATFORM2_Y, PLATFORM_IMAGE_PATH, PLATFORM_SPEED)
platform3 = Sprite(PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM3_X, PLATFORM3_Y, PLATFORM_IMAGE_PATH, PLATFORM_SPEED)
platform4 = Sprite(PLATFORM4_WIDTH, PLATFORM4_HEIGHT, PLATFORM4_X, PLATFORM4_Y, PLATFORM_IMAGE_PATH, PLATFORM_SPEED)
platform5 = Sprite(PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM5_X, PLATFORM5_Y, PLATFORM_IMAGE_PATH, PLATFORM_SPEED)

enemy = Sprite(ENEMY_WIDTH, 
               ENEMY_HEIGHT, 
               PLATFORM4_X + PLATFORM_WIDTH / 2 + ENEMY_WIDTH,
               PLATFORM4_Y - ENEMY_HEIGHT,
               ENEMY_IMAGE_PATH,
               ENEMY_SPEED)

coin = Sprite(COIN_WIDTH, 
              COIN_HEIGHT, 
              PLATFORM5_X + PLATFORM_WIDTH / 2 - COIN_WIDTH,
              PLATFORM5_Y - COIN_HEIGHT,
              COIN_IMAGE_PATH,
              COIN_SPEED)

platforms = [platform1, platform2, platform3, platform4, platform5]

game = True
finish = False
text = ""

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    if not finish:

        window.screen.blit(player.image, (player.hitbox.x, player.hitbox.y))

        window.screen.blit(platform1.image, (platform1.hitbox.x, platform1.hitbox.y))
        window.screen.blit(platform2.image, (platform2.hitbox.x, platform2.hitbox.y))
        window.screen.blit(platform3.image, (platform3.hitbox.x, platform3.hitbox.y))
        window.screen.blit(platform4.image, (platform4.hitbox.x, platform4.hitbox.y))
        window.screen.blit(platform5.image, (platform5.hitbox.x, platform5.hitbox.y))

        window.screen.blit(enemy.image, (enemy.hitbox.x, enemy.hitbox.y))

        window.screen.blit(coin.image, (coin.hitbox.x, coin.hitbox.y))

        player.controls(pygame.K_a, pygame.K_d, pygame.K_SPACE, platforms)

        player.gravity(platforms)

        finish, text = win_lose(player, coin, enemy)

    else:
        window.screen.blit(text, (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2 - 100))


    pygame.display.flip()
    window.screen.fill(BLUE)
    window.clock.tick(FPS)