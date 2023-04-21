from constants import*
from functions import*
from Window import*
from Boss import*
from Player import*
from Fireball import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE)

boss = Boss(BOSS_WIDTH, BOSS_HEIGHT, BOSS_X, BOSS_Y, BOSS_PATH, BOSS_SPEED)
player = Player(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_X, PLAYER_Y, PLAYER_PATH, PLAYER_SPEED)
fireballs = []

game = True
finish = False
text = ""

while game:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False

    if not finish:
        window.screen.blit(boss.image, (boss.hitbox.x, boss.hitbox.y))
        window.screen.blit(player.image, (player.hitbox.x , player.hitbox.y))

        player.controls(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        boss.fire(fireballs)

        draw_fireballs(window.screen, fireballs)
        move_fireballs(fireballs)

        collsions(player, boss, fireballs)
        finish, text = win_lose()
    else:
        window.screen.blit(text, (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2 - 50))

    pygame.display.flip()
    window.screen.fill(BLUE)
    window.clock.tick(FPS)
