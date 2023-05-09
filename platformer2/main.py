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
player = Player(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_X, PLAYER_Y, PLAYER_IMAGE_PATH, PLAYER_SPEED)

# Створюється 5 платформ
# Четверта платформа має інші розміри, тому у неї свої константи розміру
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

# Створюється 3 монети
# Координати кожної монети залежать від координат платформ
coin1 = Sprite(COIN_WIDTH, COIN_HEIGHT, 
                   COIN1_X, COIN1_Y, 
                   COIN_IMAGE_PATH, COIN_SPEED)

coin2 = Sprite(COIN_WIDTH, COIN_HEIGHT, 
                   COIN2_X, COIN2_Y, 
                   COIN_IMAGE_PATH, COIN_SPEED)

coin3 = Sprite(COIN_WIDTH, COIN_HEIGHT, 
                   COIN3_X, COIN3_Y, 
                   COIN_IMAGE_PATH, COIN_SPEED)


# Створюємо ворога
# Ворог з'являється на четвертій платформі
# Тому координати залежать від координат платформи 4
enemy = Sprite(ENEMY_WIDTH, ENEMY_HEIGHT, 
                   ENEMY_X, ENEMY_Y, 
                   ENEMY_IMAGE_PATH, ENEMY_SPEED)


# Кладемо всі платформи та монети в списки
# Це треба для зручного малювання платформ і перевірки колізій
platforms = [platform1, platform2, platform3, platform4, platform5]
coins = [coin1, coin2, coin3]

# шрифт для лічильника
font = pygame.font.Font(None, 40)
# змінна, яка відповідає за закриття вікна
game = True
# змінна, яка відповідає за перемикання на фінальний екран
finish = False
# текст на фінальному екрані
text = ""
# зберігає кількість зібраних монет
scores = 0


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
        # створюємо текст для лічильника балів
        scores_text = font.render(f"Бали: {scores}", True, BLACK)

        # малюємо гравця
        window.screen.blit(player.image, (player.hitbox.x, player.hitbox.y))
        # малюємо ворогка
        window.screen.blit(enemy.image, (enemy.hitbox.x, enemy.hitbox.y))

        # малюємо платформи
        draw_platforms(window.screen, platforms)
        # малюємо монети
        draw_coins(window.screen, coins)
        
        # малюємо лічильник
        window.screen.blit(scores_text, (100, 100))

        # запускаємо керування гравцем
        # розкладка: A - вліво, D - вправо, пробіл - стрибок
        player.controls(pygame.K_SPACE, pygame.K_a, pygame.K_d, platforms)

        # також запускаємо гравітацію
        player.gravity(platforms)

        scores = collisions(player, coins, scores)

        # перевіряємо чи виникла поразка чи перемога
        finish, text = win_lose(player, enemy, scores)

    # якщо гра закінчилась перемогою чи поразкою
    else:
        # малюємо тільки текст
        window.screen.blit(text, (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2 - 50))

    # оновлюємо вікно і перемальовуємо об'єкти
    pygame.display.flip()
    # заливаємо фон вікна синім кольором
    window.screen.fill(BLUE)
    # тікає годинник, які вказує, коли треба змінювати кадри
    # FPS вказує, скільки кадрів треба оновити під час тіку
    window.clock.tick(FPS)
    

    