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
font = pygame.font.Font(None, 30)
player_hp = 3
boss_hp = 3

while game:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False

    if not finish:

        player_hp_text = font.render(f"Життя гравця: {player_hp}", True, BLACK)
        boss_hp_text = font.render(f"Життя босса: {boss_hp}", True, BLACK)


        window.screen.blit(boss.image, (boss.hitbox.x, boss.hitbox.y))
        window.screen.blit(player.image, (player.hitbox.x , player.hitbox.y))

        window.screen.blit(player_hp_text, (PLAYER_HP_TEXT_X, PLAYER_HP_TEXT_Y))
        window.screen.blit(boss_hp_text, (BOSS_HP_TEXT_X, BOSS_HP_TEXT_X))       

        player.controls(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        boss.fire(fireballs)

        

        draw_fireballs(window.screen, fireballs)
        move_fireballs(fireballs)

        player_hp, boss_hp = collisions(player, boss, fireballs, player_hp, boss_hp)
        finish, text = win_lose(player_hp, boss_hp)
    else:
        window.screen.blit(text, (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2 - 50))

    pygame.display.flip()
    window.screen.fill(BLUE)
    window.clock.tick(FPS)
