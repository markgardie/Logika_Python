import pygame as pg
from constants import*
from Enemy import*
from random import randint

# функція для створення ворогів
def create_enemies():

    # розглядаємо наших ворогів у вигляді групи
    # створюємо нову групу спрайтів
    enemies = pg.sprite.Group()

    # повторюємо стільки разів, скільки хочемо створити ворогів
    for i in range(ENEMY_NUMBER):
        
        # вороги з'являються у випадковому x
        x = randint(80, WINDOW_WIDTH - 80)
        # швидкість також випадкова, але не більше 5, тобто не більше швидкості гравця
        speed = randint(1, 5)

        # створюємо нового ворога
        # задаємо його розміри, координати, шлях до зображення та швидкість
        enemy = Enemy(ENEMY_WIDTH, ENEMY_HEGHT, x, ENEMY_Y, ENEMY_IMAGE_PATH, speed)

        # додаємо ворога в групу
        enemies.add(enemy)

    # повертаємо групу ворогів для роботи з ними в main
    return enemies

# функція для перевірки зіткнень 
def collisions(enemies, bullets):

    # функція, яка допомогає перевірити зіткнення двох груп
    # повертає у вигляді пари, хто з ким зіткнувся
    # параметри True визначають, чи знищувати елементи певної групи при зіткненні
    collides = pg.sprite.groupcollide(enemies, bullets, True, True)

    # перебираємо всі пари зіткнень
    for c in collides:
        # куля зіткнулась з ворогом, отже отримуємо бал
        scores[0] += 1

        # ворог знищився, але треба знову заспавнити
        # генеруємо випадковий x
        x = randint(ENEMY_X_START, ENEMY_X_END)
        # також генеруємо випадкову швидкість
        speed = randint(1, 5)

        # створюємо нового ворога
        enemy = Enemy(ENEMY_WIDTH, ENEMY_HEGHT, x, ENEMY_X_START, ENEMY_IMAGE_PATH, speed)

        # додаємо його в групу ворогів
        enemies.add(enemy)

# перевірка перемоги
def win(finish, text):
    # якщо ми досягли цілі по балам
    if scores[0] >= GOAL:
        # зміна-флаг призупиняє гру
        finish = True
        
        # шрифт для тексту
        font = pg.font.Font(None, 50)

        # створюємо сам текст перемоги
        text = font.render(WIN_TEXT, True, TEXT_COLOR)

    # повертаємо створенний текст та змінну-флаг для використання в main
    return finish, text

# перевірка поразки
def lose(finish, text):
    # якщо ми пропустили більше ніж максимум пропущених
    if miss[0] >= MAX_MISS:
        # зміна-флаг призупиняє гру
        finish = True

        # шрифт для тексту
        font = pg.font.Font(None, 50)

        # створюємо сам текст перемоги
        text = font.render(LOSE_TEXT, True, TEXT_COLOR)
    
    # повертаємо створенний текст та змінну-флаг для використання в main
    return finish, text