from constants import*
import pygame


# функція перемоги-поразки
# в параметрах отримуємо життя босса та гравця
def win_lose(player_hp, boss_hp):

    # змінна, яка відповідає за переключення на фінальний екран
    # поки переключення немає
    finish = False

    # текст на фінальному екрані
    text = ""

    # створення шрифта для роботи з текстом
    # стандратний шрифт (None), розмір 50
    font = pygame.font.Font(None, 50)

    # якщо у гравця 0 або менше здоров'я
    if player_hp <= 0:
        # переключаємось на фінальний екран
        finish = True
        # створюємо текст поразки
        text = font.render("Поразка", True, BLACK)

    # якщо у босса 0 або менше здоров'я
    if boss_hp <= 0:
        # переключаємось на фінальний екран
        finish = True
        # створюємо текст перемоги
        text = font.render("Перемога", True, BLACK)

    return finish, text

# малювання фаєрболів
# для цього в параметрах отримуємо список фаєрболів
def draw_fireballs(window, fireballs):

    # проходимось по списку фаєрболів
    for fireball in fireballs:
        # і малюємо картинку кожного фаєрбола
        # в координатах хітбокса фаєрбола
        window.blit(fireball.image, (fireball.hitbox.x, fireball.hitbox.y))

# рух фаєрболів
def move_fireballs(fireballs):
    # проходимось по всім фаєрболам
    for fireball in fireballs:
        # запускаємо вже готовий метод руху
        fireball.move()

# перевірка зіткнень
# в параметрах отримуємо об'єкти, які приймають участь в зіткненнях: босс, гравець, фаєрболи
# також отримуємо змінні здоров'я гравця та боса, оскільки вони повинні змінюватись
def collisions(player, boss, fireballs, player_hp, boss_hp):

    # проходимось по всім фаєрболам
    for fireball in fireballs:

        # якщо якийсь фаєрбол торкається гравця
        if player.hitbox.colliderect(fireball.hitbox):
            # віднімається одне життя у гравця
            player_hp -= 1
            # фаєрбол пропадає
            fireballs.remove(fireball)

     # якщо гравець торкається босс
    if player.hitbox.colliderect(boss.hitbox):
        # віднімається одне життя у босса
        boss_hp -= 1
        # босс переміщується у випадкову точку
        boss.move()

    return player_hp, boss_hp
