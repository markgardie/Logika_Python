import pygame
from constants import*

pygame.init()


# функція перемоги_поразки
# в параметрах приймає гравця та монету
def win_lose(player, coin, enemy):

    # аби працювати з текстом, треба спочатку створити шрифт
    # стандартний шрифт (None), розмір 50
    font = pygame.font.Font(None, 50)

    # змінна, яка відповідає за переключення на фінальний екран
    # коли ця змінна стає True, то перемикається фінальний екран
    finish = False
    # текст, який буде на фінальному екрані
    text = ""

    # якщо гравець торкається монети 
    if player.hitbox.colliderect(coin.hitbox):
        # перемикаємось на фінальний екран
        finish = True
        # ми перемагаємо
        text = font.render("Ти переміг", True, BLACK)

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


    # повертаємо ці змінні в main
    # перемикання на фінальний екран і вивід тексту відбуваються в main
    return finish, text