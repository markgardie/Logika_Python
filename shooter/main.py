from Window import*
from Sprite import*
from Player import*
from constants import*
from functions import create_enemies, win, collisions, lose

# створюємо вікно
window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BACKGROUND_IMAGE_PATH)

# створюємо гравця
player = Player(PLAYER_WIDTH, PLAYER_HEIGHT, WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80, PLAYER_IMAGE_PATH, PLAYER_SPEED)
# за допомогою функції створюємо групу ворогів і заповнюємо її
enemies = create_enemies()

# створюємо групу куль, але тут вона поки пустп
bullets = pg.sprite.Group()

# запускаємо фонову музику
BACKGROUND_SOUND.play()

# змінна-флаг, яка закриває повністю гру та вікно
game = True
# змінна-флаг, яка прибирає всі об'єкти з екрану і залишає екран перемоги чи поразки
finish = False
# текст перемоги чи поразки
text = ""

# ігровий цикл
while game:

    # цикл перебирає виникаючі події
    for event in pg.event.get():
        # подія натискання на крестик
        if event.type == pg.QUIT:
            # закриття гри та вікна при натисканні на крестик
            game = False
        # подія натискання на клавіатуру + клавіша пропуск
        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            # запускається звук пострілу
            FIRE_SOUND.play()
            # створюється нова куля, гравець стріляє
            player.fire(bullets)

    # якщо гра не завершилась (перемогою чи поразкою)
    if not finish:

        # малюємо фон
        window.screen.blit(window.bg_image, (0, 0))
        # малюємо гравця
        window.screen.blit(player.image, (player.rect.x, player.rect.y))
        # малюємо групу ворогів
        enemies.draw(window.screen)
        # малюємо групу куль
        bullets.draw(window.screen)

        # створюємо текст лічильника пропущених ворогів
        miss_text = FONT.render(f"{MISS_TEXT} {miss[0]}", True, TEXT_COLOR)
        # створюємо текст лічильника балів
        scores_text = FONT.render(f"{SCORES_TEXT} {scores[0]}", True, TEXT_COLOR)

        # малюємо обидва лічильники
        window.screen.blit(miss_text, MISS_TEXT_COR)
        window.screen.blit(scores_text, SCORES_TEXT_COR)

        # запускаємо керування гравця
        # в дужках можна задавати будь-яку розкладку керування
        player.control(pg.K_a, pg.K_d)
        # рух групи ворогів
        enemies.update()
        # рух групи куль
        bullets.update()

        # перевірка колізій
        collisions(enemies, bullets)
        # перевіряємо перемогу та поразку
        # результати записуємо в змінні finish, text
        finish, text = win(finish, text)
        finish, text = lose(finish, text)
    # якщо гра завершилась (перемогою чи поразкою)
    else:
        # все ще малюємо фон
        window.screen.blit(window.bg_image, (0, 0))
        # малюємо текст перемоги чи поразки
        window.screen.blit(text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        # зупиняємо фонову музику
        BACKGROUND_SOUND.stop()

        # більше ніяки об'єкти на екрані не повинні з'являтись
        # тому їх не малюємо


    # оновлюємо екран
    pg.display.update()
    # запускаємо тіки годинника
    window.clock.tick(FPS)