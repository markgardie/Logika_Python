import pygame
from constants import*

pygame.init()

# функція малює на екрін снаряди
# в параметрах вона приймає 2 списки куль
# bullets1 - снаряди першого танку
# bullets2 - снаряди другого танку 
def draw_bullets(window, bullets1, bullets2):
    
    # циклом for проходимось по всім снарядам першого танку
    for bullet in bullets1:
        # малюємо кожен снаряд
        # малюємо саме картинку, а не весь спрайт
        # координати же беремо у хітбокса снаряду
        window.blit(bullet.image, (bullet.hitbox.x, bullet.hitbox.y))
    
    # циклом for проходимось по всім снарядам другого танку
    for bullet in bullets2:
        # малюємо кожен снаряд
        # малюємо саме картинку, а не весь спрайт
        # координати же беремо у хітбокса снаряду
        window.blit(bullet.image, (bullet.hitbox.x, bullet.hitbox.y))

# функція для руху снарядів
# в параметрах приймає 2 списки снарядів
# bullets1 - снаряди першого танку
# bullets2 - снаряди другого танку 
def move_bullets(bullets1, bullets2):
    
    # циклом for проходимось по всім снарядам першого танку
    for bullet in bullets1:
        # рухаємо снаряди першого танку
        # виставляємо напрямок 1
        # це напрямок направо
        bullet.move(1)
    
    # циклом for проходимось по всім снарядам другого танку
    for bullet in bullets2:
        # рухаємо снаряди друого танку
        # виставляємо напрямок -1
        # це напрямок наліво
        bullet.move(-1)

# функція перемоги_поразки
# в параметрах приймає 2 списки снарядів та 2 гравців
def win_lose(player1, player2, bullets1, bullets2):

    # змінна, яка відповідає за переключення на фінальний екран
    # коли ця змінна стає True, то перемикається фінальний екран
    finish = False
    # текст, який буде на фінальному екрані
    text = ""

    # аби працювати з текстом, треба спочатку створити шрифт
    # стандартний шрифт (None), розмір 50
    font = pygame.font.Font(None, 50)

    # циклом for проходимось по всім снарядам першого танку
    for bullet in bullets1:
        # якщо другий танк торкається якогось снарядку
        if player2.hitbox.colliderect(bullet.hitbox):
            # перемикаємось на фінальний екран
            finish = True
            # перемагає перший танк
            text = font.render("Переміг гравець 1", True, BLACK)

    # циклом for проходимось по всім снарядам другого танку
    for bullet in bullets2:
        
        # якщо перший танк торкається якогось снарядку
        if player1.hitbox.colliderect(bullet.hitbox):
            # перемикаємось на фінальний екран
            finish = True
            # перемагає другий танк
            text = font.render("Переміг гравець 2", True, BLACK)

    # якщо перший танк торкається друого танку
    if player1.hitbox.colliderect(player2.hitbox):
            # перемикаємось на фінальний екран
            finish = True
            # нічия
            text = font.render("Нічия", True, BLACK)

    # повертаємо ці змінні в main
    # перемикання на фінальний екран і вивід тексту відбуваються в main
    return finish, text


