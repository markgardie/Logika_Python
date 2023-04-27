from constants import*
from functions import*
from Window import*
from Sprite import*
from Player import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE)

player = Player(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_X, PLAYER_Y, PLAYER_IMAGE_PATH, PLAYER_SPEED)

platform1 = Sprite(PLATFORM_WIDTH, PLATFORM_HEIGHT, 
                   PLATFORM1_X, PLATFORM1_Y, 
                   PLATFORM_IMAGE_PATH, PLATFORM_SPEED)

platform2 = Sprite(PLATFORM_WIDTH, PLATFORM_HEIGHT, 
                   PLATFORM2_X, PLATFORM2_Y, 
                   PLATFORM_IMAGE_PATH, PLATFORM_SPEED)

platform3 = Sprite(PLATFORM_WIDTH, PLATFORM_HEIGHT, 
                   PLATFORM3_X, PLATFORM3_Y, 
                   PLATFORM_IMAGE_PATH, PLATFORM_SPEED)

platform4 = Sprite(PLATFORM4_WIDTH, PLATFORM4_HEIGHT, 
                   PLATFORM4_X, PLATFORM4_Y, 
                   PLATFORM_IMAGE_PATH, PLATFORM_SPEED)

platform5 = Sprite(PLATFORM_WIDTH, PLATFORM_HEIGHT, 
                   PLATFORM5_X, PLATFORM5_Y, 
                   PLATFORM_IMAGE_PATH, PLATFORM_SPEED)

coin1 = Sprite(COIN_WIDTH, COIN_HEIGHT, 
                   COIN1_X, COIN1_Y, 
                   COIN_IMAGE_PATH, COIN_SPEED)

coin2 = Sprite(COIN_WIDTH, COIN_HEIGHT, 
                   COIN2_X, COIN2_Y, 
                   COIN_IMAGE_PATH, COIN_SPEED)

coin3 = Sprite(COIN_WIDTH, COIN_HEIGHT, 
                   COIN3_X, COIN3_Y, 
                   COIN_IMAGE_PATH, COIN_SPEED)


enemy = Sprite(ENEMY_WIDTH, ENEMY_HEIGHT, 
                   ENEMY_X, ENEMY_Y, 
                   ENEMY_IMAGE_PATH, ENEMY_SPEED)


platforms = [platform1, platform2, platform3, platform4, platform5]
coins = [coin1, coin2, coin3]

font = pygame.font.Font(None, 40)
game = True
finish = False
text = ""
scores = 0

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if not finish:
        scores_text = font.render(f"Бали: {scores}", True, BLACK)

        window.screen.blit(player.image, (player.hitbox.x, player.hitbox.y))
        window.screen.blit(enemy.image, (enemy.hitbox.x, enemy.hitbox.y))

        draw_platforms(window.screen, platforms)
        draw_coins(window.screen, coins)
        
        window.screen.blit(scores_text, (100, 100))

        player.controls(pygame.K_SPACE, pygame.K_a, pygame.K_d, platforms)
        player.gravity(platforms)

        scores = collisions(player, coins, scores)
        finish, text = win_lose(player, enemy, scores)
    else:
        window.screen.blit(text, (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2 - 50))

    pygame.display.flip()
    window.screen.fill(BLUE)
    window.clock.tick(FPS)
    

    