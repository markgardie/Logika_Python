from constants import*
from functions import*
from Window import*
from Sprite import*
from Player import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE)

player = Player(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_X, PLAYER_Y, PLAYER_IMAGE_PATH, PLAYER_SPEED)

platform1 = Sprite(PLAYER_WIDTH, PLAYER_HEIGHT, 
                   PLATFORM1_X, PLATFORM1_Y, 
                   PLATFORM_IMAGE_PATH, PLATFORM_SPEED)

platform2 = Sprite(PLAYER_WIDTH, PLAYER_HEIGHT, 
                   PLATFORM2_X, PLATFORM2_Y, 
                   PLATFORM_IMAGE_PATH, PLATFORM_SPEED)

platform3 = Sprite(PLAYER_WIDTH, PLAYER_HEIGHT, 
                   PLATFORM3_X, PLATFORM3_Y, 
                   PLATFORM_IMAGE_PATH, PLATFORM_SPEED)

platform4 = Sprite(PLAYER_WIDTH, PLAYER_HEIGHT, 
                   PLATFORM4_X, PLATFORM4_Y, 
                   PLATFORM_IMAGE_PATH, PLATFORM_SPEED)

platform5 = Sprite(PLAYER_WIDTH, PLAYER_HEIGHT, 
                   PLATFORM5_X, PLATFORM5_Y, 
                   PLATFORM_IMAGE_PATH, PLATFORM_SPEED)


coin1 = Sprite(COIN_WIDTH, COIN_HEIGHT, COIN1_X, COIN1_Y, COIN_IMAGE_PATH, COIN_SPEED)
coin2 = Sprite(COIN_WIDTH, COIN_HEIGHT, COIN2_X, COIN2_Y, COIN_IMAGE_PATH, COIN_SPEED)
coin3 = Sprite(COIN_WIDTH, COIN_HEIGHT, COIN3_X, COIN3_Y, COIN_IMAGE_PATH, COIN_SPEED)

platforms = [platform1, platform2, platform3, platform4, platform5]
coins = [coin1, coin2, coin3]

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

        window.screen.blit(player.image, (player.hitbox.x, player.hitbox.y))

        window.screen.blit(platform1.image, (platform1.hitbox.x, platform1.hitbox.y))
        window.screen.blit(platform2.image, (platform2.hitbox.x, platform2.hitbox.y))
        window.screen.blit(platform3.image, (platform3.hitbox.x, platform3.hitbox.y))
        window.screen.blit(platform4.image, (platform4.hitbox.x, platform4.hitbox.y))
        window.screen.blit(platform5.image, (platform5.hitbox.x, platform5.hitbox.y))

        window.screen.blit(coin1.image, (coin1.hitbox.x, coin1.hitbox.y))
        window.screen.blit(coin2.image, (coin2.hitbox.x, coin2.hitbox.y))
        window.screen.blit(coin3.image, (coin3.hitbox.x, coin3.hitbox.y))

        window.screen.blit(counter_text, (100, 100))

        collisions(player, coins)
        player.controls(pygame.K_SPACE, pygame.K_a, pygame.K_d, platforms)
        player.gravity(platforms)

    else:
        window.screen.blit(text, (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2 - 50))

    pygame.display.flip()
    window.screen.fill(BLUE)
    window.clock.tick(FPS)
    

    