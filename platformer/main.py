from constants import*
from functions import*
from Window import*
from Sprite import*
from Player import*

# Створюємо вікно
# з синім фоном
window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, BLUE, CAPTION)

# Створюємо гравця
# Гравець з'являється на першій платформі
# Тому координати залежать від координат платформи 1
player = Player(PLAYER_WIDTH, 
                PLAYER_HEIGHT, 
                PLATFORM1_X + PLATFORM_WIDTH / 2 - PLAYER_WIDTH, 
                PLATFORM1_Y - PLAYER_HEIGHT, 
                PLAYER_IMAGE_PATH, 
                PLAYER_SPEED)

# Створюється 5 платформ
# Четверта платформа має інші розміри, тому у неї свої константи
platform1 = Sprite(PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM1_X, PLATFORM1_Y, PLATFORM_IMAGE_PATH, PLATFORM_SPEED)
platform2 = Sprite(PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM2_X, PLATFORM2_Y, PLATFORM_IMAGE_PATH, PLATFORM_SPEED)
platform3 = Sprite(PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM3_X, PLATFORM3_Y, PLATFORM_IMAGE_PATH, PLATFORM_SPEED)
platform4 = Sprite(PLATFORM4_WIDTH, PLATFORM4_HEIGHT, PLATFORM4_X, PLATFORM4_Y, PLATFORM_IMAGE_PATH, PLATFORM_SPEED)
platform5 = Sprite(PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM5_X, PLATFORM5_Y, PLATFORM_IMAGE_PATH, PLATFORM_SPEED)

# Створюємо ворога
# Ворог з'являється на четвертій платформі
# Тому координати залежать від координат платформи 4
enemy = Sprite(ENEMY_WIDTH, 
               ENEMY_HEIGHT, 
               PLATFORM4_X + PLATFORM_WIDTH / 2 + ENEMY_WIDTH,
               PLATFORM4_Y - ENEMY_HEIGHT,
               ENEMY_IMAGE_PATH,
               ENEMY_SPEED)

# Створюємо монету
# Монета знаходиться на платформі 5
# Тому в координатах фігурують координати платформи 5
coin = Sprite(COIN_WIDTH, 
              COIN_HEIGHT, 
              PLATFORM5_X + PLATFORM_WIDTH / 2 - COIN_WIDTH,
              PLATFORM5_Y - COIN_HEIGHT,
              COIN_IMAGE_PATH,
              COIN_SPEED)

# Кладемо всі платформи в список
# Це треба для зручного малювання платформ і перевірки колізій
platforms = [platform1, platform2, platform3, platform4, platform5]

# змінна, яка відповідає за закриття вікна
game = True
# змінна, яка відповідає за перемикання на фінальний екран
finish = False
# текст на фінальному екрані
text = ""

# ігровий цикл
while game:
      # цикл перебирає виникаючі події
    for event in pygame.event.get():
        # подія натискання на крестик
        if event.type == pygame.QUIT:
            # закриття гри та вікна при натисканні на крестик
            game = False
    
    # якщо гра не закінчилась перемогою чи поразкою
    if not finish:

        # малюємо гравця
        window.screen.blit(player.image, (player.hitbox.x, player.hitbox.y))

        # малюємо платформи
        window.screen.blit(platform1.image, (platform1.hitbox.x, platform1.hitbox.y))
        window.screen.blit(platform2.image, (platform2.hitbox.x, platform2.hitbox.y))
        window.screen.blit(platform3.image, (platform3.hitbox.x, platform3.hitbox.y))
        window.screen.blit(platform4.image, (platform4.hitbox.x, platform4.hitbox.y))
        window.screen.blit(platform5.image, (platform5.hitbox.x, platform5.hitbox.y))

        # малюємо ворога
        window.screen.blit(enemy.image, (enemy.hitbox.x, enemy.hitbox.y))

        # малюємо моенту
        window.screen.blit(coin.image, (coin.hitbox.x, coin.hitbox.y))

        # запускаємо керування гравцем
        # розкладка: A - вліво, D - вправо, пробіл - стрибок
        player.controls(pygame.K_a, pygame.K_d, pygame.K_SPACE, platforms)

        # також запускаємо гравітацію
        player.gravity(platforms)

        # перевіряємо чи виникла поразка чи перемога
        finish, text = win_lose(player, coin, enemy)

    # якщо гра закінчилась перемогою чи поразкою
    else:
        # малюємо тільки текст
        window.screen.blit(text, (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2 - 100))


    # оновлюємо вікно і перемальовуємо об'єкти
    pygame.display.flip()
    # заливаємо фон вікна синім кольором
    window.screen.fill(BLUE)
    # тікає годинник, які вказує, коли треба змінювати кадри
    # FPS вказує, скільки кадрів треба оновити під час тіку
    window.clock.tick(FPS)