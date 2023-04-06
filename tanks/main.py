from Tank import *
from Window import*
from functions import*
from Bullet import*
from constants import*
import time

# Створюємо вікно
# з синім фоном
window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, BLUE, CAPTION)

# створюємо першого гравця
# координата y однакова у всіх танках
# вони з'являються на однаковій висоті, посередині
tank1 = Tank(TANK_WIDTH, TANK_HEIGHT, TANK1_X, TANKS_Y, TANK1_IMAGE_PATH, PLAYER_SPEED)
# створюємо другого гравця
tank2 = Tank(TANK_WIDTH, TANK_HEIGHT, TANK2_X, TANKS_Y, TANK2_IMAGE_PATH, PLAYER_SPEED)

# створюємо стіни
# перші дві стіни вертикальні, тому стоїть буква V - vertical
wall1 = Sprite(V_WALL_WIDTH, V_WALL_HEIGHT, WALL1_X, WALL1_Y, WALL_IMAGE_PATH, WALL_SPEED)
wall2 = Sprite(V_WALL_WIDTH, V_WALL_HEIGHT, WALL2_X, WALL2_Y, WALL_IMAGE_PATH, WALL_SPEED)

# останні дві стіни горизонтальні, H - horizontal
wall3 = Sprite(H_WALL_WIDTH, H_WALL_HEIGHT, WALL3_X, WALL3_Y, WALL_IMAGE_PATH, WALL_SPEED)
wall4 = Sprite(H_WALL_WIDTH, H_WALL_HEIGHT, WALL4_X, WALL4_Y, WALL_IMAGE_PATH, WALL_SPEED)

# списки снарядів першого та другого танків
# напочатку гри пусті, оскільки ще не було вистрілів
bullets1 = []
bullets2 = []

# список стін
# для зручного користування в функціях колізій
walls = [wall1, wall2, wall3, wall4]

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
        # подія натискання на клавішу Е
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            # якщо це клавіша Е, то це стріляє перший танк
            # передаємо в дужках список снарядів першого танку
            # всередині функції цей список заповнюється
            tank1.fire1(bullets1)
        # подія натискання на клавішу L
        if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            # якщо це клавіша L, то це стріляє другий танк
            tank2.fire2(bullets2)

    # якщо гра не закінчилась перемогою чи поразкою
    if not finish:
        
        # малюємо перший танк
        window.screen.blit(tank1.image, (tank1.hitbox.x, tank1.hitbox.y))
        # малюємо другий танк
        window.screen.blit(tank2.image, (tank2.hitbox.x, tank2.hitbox.y))
        # малюємо снаряди всіх танків
        draw_bullets(window.screen, bullets1, bullets2)

        # малюємо стінки
        window.screen.blit(wall1.image, (wall1.hitbox.x, wall1.hitbox.y))
        window.screen.blit(wall2.image, (wall2.hitbox.x, wall2.hitbox.y))
        window.screen.blit(wall3.image, (wall3.hitbox.x, wall3.hitbox.y))
        window.screen.blit(wall4.image, (wall4.hitbox.x, wall4.hitbox.y))

        # рухаємо снаряди
        move_bullets(bullets1, bullets2)

        # перевіряємо колізії снарядів зі стінами
        wall_collisions(walls, bullets1, bullets2)

        # керування першим танком
        # розкладка: WASD
        tank1.controls(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        # керування другим танком
        # розкладка: стрілки
        tank2.controls(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)

        # перевірка чи була перемога чи поразка
        finish, text = win_lose(tank1, tank2, bullets1, bullets2, walls)

    # якщо гра закінчилась перемогою чи поразкою
    else:
        # малюємо тільки текст
        window.screen.blit(text, (WINDOW_WIDTH / 2 - 150, WINDOW_HEIGHT / 2 - 80))

    # оновлюємо вікно і перемальовуємо об'єкти
    pygame.display.flip()
    # заливаємо фон вікна синім кольором
    window.screen.fill(BLUE)
    # тікає годинник, які вказує, коли треба змінювати кадри
    # FPS вказує, скільки кадрів треба оновити під час тіку
    window.clock.tick(FPS)