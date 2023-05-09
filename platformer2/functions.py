from constants import*
import pygame

# функція перемоги_поразки
def win_lose(player, enemy, scores):

    # аби працювати з текстом, треба спочатку створити шрифт
    # стандартний шрифт (None), розмір 50
    font = pygame.font.Font(None, 50)
    # змінна, яка відповідає за переключення на фінальний екран
    # коли ця змінна стає True, то перемикається фінальний екран
    finish = False
    # текст, який буде на фінальному екрані
    text = ""

    # якщо зібрали всі 3 монети
    if scores >= 3:
        # перемикаємось на фінальний екран 
        finish = True
        # перемога
        text = font.render(WIN_TEXT, True, BLACK)

    # якщо гравець торкається ворога 
    if player.hitbox.colliderect(enemy.hitbox):
        # перемикаємось на фінальний екран
        finish = True
        # ми програємо
        text = font.render("Поразка", True, BLACK)

    # якщо гравець торкається нижньої межі (висота вікна) 
    if player.hitbox.y >= WINDOW_HEIGHT - 10:

        # перемикаємось на фінальний екран
        finish = True
        # поразка
        text = font.render("Поразка", True, BLACK)


    return finish, text

# перевірка торкань гравця та монет
def collisions(player, coins, scores):

    # циклом проходимось по всім монетам в списку
    for coin in coins:
        # якщо гравець торкається якоїсь монети
        if player.hitbox.colliderect(coin.hitbox):
            # збільшуємо бали
            scores += 1
            # прибираємо зібрану моенту
            coins.remove(coin)

    return scores

# малювання платформ
def draw_platforms(window, platforms):

    # циклом проходимось по всім платформам в списку
    for platform in platforms:
        # малюємо кожну платформу
        # беремо зображення платформи і малюємо в координатах хітбокса платформи
        window.blit(platform.image, (platform.hitbox.x, platform.hitbox.y))

# малювання моент
def draw_coins(window, coins):

    # циклом проходимось по всім монетам в списку
    for coin in coins:
        # малюємо кожну монету
        # беремо зображення монети і малюємо в координатах хітбокса монети
        window.blit(coin.image, (coin.hitbox.x, coin.hitbox.y))
        

        