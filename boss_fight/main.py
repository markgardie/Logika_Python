from constants import*
from functions import*
from Window import*
from Boss import*
from Player import*
from Fireball import*

# створюємо об'єкти вікна, босса, гравця
window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE)
boss = Boss(BOSS_WIDTH, BOSS_HEIGHT, BOSS_X, BOSS_Y, BOSS_PATH, BOSS_SPEED)
player = Player(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_X, PLAYER_Y, PLAYER_PATH, PLAYER_SPEED)

# створюємо список фаєрболів, оскільки їх буде багато
# фаєрболів напочатку гри немає, тому він пустий
fireballs = []

# змінна, яка відповідає за запуск та закриття гри
game = True
# змінна, яка відповідає за перемикання на фінальний екран
finish = False
# текст на фінальному екрані
text = ""
# шрифт для тексту лічильників
font = pygame.font.Font(None, 30)

# життя гравця та босса
player_hp = 3
boss_hp = 3

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

        # створюємо тексти лічильників життя гравця та босса
        # тут використовуємо f-строку, яка дозволяє в строку (текст) вставити значення змінної
        # ми вставляємо в текст конкретну кількість життів
        player_hp_text = font.render(f"Життя гравця: {player_hp}", True, BLACK)
        boss_hp_text = font.render(f"Життя босса: {boss_hp}", True, BLACK)

        # малювання картинки босса
        # в координатах хітбокса
        window.screen.blit(boss.image, (boss.hitbox.x, boss.hitbox.y))

        # теж саме, але для гравця
        window.screen.blit(player.image, (player.hitbox.x , player.hitbox.y))

        # малювання текстів лічильників
        window.screen.blit(player_hp_text, (PLAYER_HP_TEXT_X, PLAYER_HP_TEXT_Y))
        window.screen.blit(boss_hp_text, (BOSS_HP_TEXT_X, BOSS_HP_TEXT_X))       

        # запуск керування
        # розкладка WASD
        player.controls(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)

        # постріли босса
        boss.fire(fireballs)

        # малювання фаєрболів
        draw_fireballs(window.screen, fireballs)
        # рух фаєрболів
        move_fireballs(fireballs)

        # запуск перевірки колізій
        player_hp, boss_hp = collisions(player, boss, fireballs, player_hp, boss_hp)
        # перевірка перемоги чи поразки
        finish, text = win_lose(player_hp, boss_hp)
    
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
