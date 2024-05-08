import random
import pygame
import os

pygame.mixer.init()
asitwas = pygame.mixer.Sound('sound/Harry Styles - As It Was.mp3')
asitwas.set_volume(0.3)

asitwas.play()

pygame.init()

WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode([WIDTH, HEIGHT])
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption('Jetpack Joyride Remake in Python!')
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)
bg_color = (128, 128, 128)
lines = [0, WIDTH / 4, 2 * WIDTH / 4, 3 * WIDTH / 4]
game_speed = 3
pause = False
init_y = HEIGHT - 130
player_y = init_y
enemy_y = init_y
booster = False
counter = 0
y_velocity = 0
gravity = 0.4
new_laser = True
laser = []
distance = 0
restart_cmd = False
new_bg = 0
coins = []
coin_count = 0  # Ініціалізуємо лічильник монеток
enemies = []
accelerations = []
decelerations = []
acceleration_active = False
deceleration_active = False
speed_boost_time = 0
speed_reduction_time = 0

def move_enemies(self):
    self.x -= self.speed  # Вороги рухаються тільки вліво

def draw_enemies(self, screen):
    screen.blit(self.image, (self.x, self.y))

def generate_enemy():
    line = random.choice([0, 1, 2, 3])  # Вибір лінії для руху ворога
    return line, enemy_image


PROJECT_PATH = os.path.abspath(__file__ + "/..")
PLAY_PATH = os.path.join(PROJECT_PATH, "play")

COIN_IMAGE_PATH = os.path.join(PLAY_PATH, "coin.png")
PLAYER_IMAGE_PATH = os.path.join(PLAY_PATH, "player.png")
ENEMY_IMAGE_PATH = os.path.join(PLAY_PATH, "enemy.png")
BACKGROUND_IMAGE_PATH = os.path.join(PLAY_PATH, "background.png")
BOOSTED_IMAGE_PATH = os.path.join(PLAY_PATH, "boosted.png")
ACCELERATION_IMAGE_PATH = os.path.join(PLAY_PATH, "acceleration.png")
DECELERATION_IMAGE_PATH = os.path.join(PLAY_PATH, "deceleration.png")

# rocket variables
rocket_counter = 0
rocket_active = False
rocket_delay = 0
rocket_coords = []

# load in player info in beginning
file = open('player_info.txt', 'r')
read = file.readlines()
high_score = int(read[0])
lifetime = int(read[1])
file.close()



def generate_coin():
    x = WIDTH + 100
    y = random.randint(100, HEIGHT - 100)
    return [x, y]

for enemy in enemies[:]:
    enemy.move()
    enemy.draw(screen)
    if enemy.x < -enemy.image.get_width():  # Якщо ворог вийшов за межі екрану, видаляємо його
        enemies.remove(enemy) 

def generate_acceleration():
    x = WIDTH + 100
    y = random.randint(100, HEIGHT - 100)
    return [x, y, acceleration_image]

def generate_deceleration():
    x = WIDTH + 100
    y = random.randint(100, HEIGHT - 100)
    return [x, y, deceleration_image]

def draw_pause():
    pygame.draw.rect(surface, (128, 128, 128, 150), [0, 0, WIDTH, HEIGHT])
    pygame.draw.rect(surface, 'dark gray', [200, 150, 600, 50], 0, 10)
    surface.blit(font.render('Game Paused. Press P to Resume', True, 'black'), (220, 160))
    screen.blit(surface, (0, 0))

# all the code to move lines across screen and draw bg images
def draw_screen(line_list, lase):
    screen.fill('black')
    pygame.draw.rect(surface, (bg_color[0], bg_color[1], bg_color[2], 50), [0, 0, WIDTH, HEIGHT])
    screen.blit(surface, (0, 0))
    top = pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 50])
    bot = pygame.draw.rect(screen, 'gray', [0, HEIGHT - 50, WIDTH, 50])
    for i, coin in enumerate(coins):
        coins[i][0] -= game_speed
        if coins[i][0] < -20:
            coins.pop(i)
    
    for acceleration in accelerations:
        screen.blit(acceleration[2][0], (acceleration[0], acceleration[1]))

    for deceleration in decelerations:
        screen.blit(deceleration[2][0], (deceleration[0], deceleration[1]))

    for i in range(len(line_list)):
        pygame.draw.line(screen, 'black', (line_list[i], 0), (line_list[i], 50), 3)
        pygame.draw.line(screen, 'black', (line_list[i], HEIGHT - 50), (line_list[i], HEIGHT), 3)
        if not pause:
            line_list[i] -= game_speed
            lase[0][0] -= game_speed
            lase[1][0] -= game_speed
        if line_list[i] < 0:
            line_list[i] = WIDTH

    for coin in coins:
        screen.blit(coin_image, (coin[0] - coin_image.get_width() // 2, coin[1] - coin_image.get_height() // 2))  # Відображаємо зображення монетки
        pygame.draw.circle(screen, 'gold', coin, 10)


    lase_line = pygame.draw.line(screen, 'yellow', (lase[0][0], lase[0][1]), (lase[1][0], lase[1][1]), 10)
    pygame.draw.circle(screen, 'yellow', (lase[0][0], lase[0][1]), 12)
    pygame.draw.circle(screen, 'yellow', (lase[1][0], lase[1][1]), 12)
    screen.blit(font.render(f'Distance: {int(distance)} m', True, 'white'), (10, 10))
    screen.blit(font.render(f'High Score: {int(high_score)} m', True, 'white'), (10, 70))
    return line_list, top, bot, lase, lase_line

background_image = pygame.image.load(BACKGROUND_IMAGE_PATH).convert()
player_image = pygame.transform.scale(pygame.image.load(PLAYER_IMAGE_PATH).convert_alpha(), (int(pygame.image.load(PLAYER_IMAGE_PATH).get_width() / 5), int(pygame.image.load(PLAYER_IMAGE_PATH).get_height() / 5)))  # Завантажуємо зменшене зображення гравця
boosted_image = pygame.transform.scale(pygame.image.load(BOOSTED_IMAGE_PATH).convert_alpha(), (int(pygame.image.load(BOOSTED_IMAGE_PATH).get_width() / 5), int(pygame.image.load(BOOSTED_IMAGE_PATH).get_height() / 5)))  # Завантажуємо зменшене зображення бустера
coin_image = pygame.transform.scale(pygame.image.load(COIN_IMAGE_PATH).convert_alpha(), (int(pygame.image.load(COIN_IMAGE_PATH).get_width() / 15), int(pygame.image.load(COIN_IMAGE_PATH).get_height() / 15)))
enemy_image = pygame.transform.scale(pygame.image.load(ENEMY_IMAGE_PATH).convert_alpha(), (int(pygame.image.load(ENEMY_IMAGE_PATH).get_width() / 15), int(pygame.image.load(ENEMY_IMAGE_PATH).get_height() / 15)))
acceleration_image = pygame.image.load(ACCELERATION_IMAGE_PATH).convert_alpha(), (int(pygame.image.load(ACCELERATION_IMAGE_PATH).get_width() / 10), int(pygame.image.load(ACCELERATION_IMAGE_PATH).get_height() / 10))
deceleration_image = pygame.image.load(DECELERATION_IMAGE_PATH).convert_alpha(), (int(pygame.image.load(DECELERATION_IMAGE_PATH).get_width() / 10), int(pygame.image.load(DECELERATION_IMAGE_PATH).get_height() / 10))

# draw player including animated states
def draw_player():
    if player_y < init_y or pause:
        if booster:
            screen.blit(boosted_image, (100, player_y))
        else:
            screen.blit(player_image, (100, player_y))
    else:
        if counter < 10:
            # Анімація руху вперед
            pass
        elif 10 <= counter < 20:
            # Анімація стояння
            screen.blit(player_image, (100, player_y))
        elif 20 <= counter < 30:
            # Анімація руху назад
            pass
        else:
            # Анімація стояння
            screen.blit(player_image, (100, player_y))

    return pygame.Rect(100, player_y, player_image.get_width(), player_image.get_height())

def draw_enemy(): 
    for enemy in enemies[:]:

 # Визначення напрямку руху
        if enemy[3] == 0:
            # Рух вправо
            enemy[0] -= enemy[2]
            enemy[1] += enemy[2] / 2
        else:
            # Рух вліво
            enemy[0] -= enemy[2]
            enemy[1] -= enemy[2] / 2

        # Відображення ворога
        enemy_rect = pygame.Rect(int(enemy[0]), int(enemy[1]), enemy_image.get_width(), enemy_image.get_height())
        screen.blit(enemy_image, enemy_rect)

        # Перевірка виходу за межі екрану
        if enemy[0] < -50 or enemy[1] < 50 or enemy[1] > HEIGHT - 50:
            enemies.remove(enemy)
 
    return pygame.Rect(100, enemy_y, enemy_image.get_width(), enemy_image.get_height())

# Додайте цей код в основному циклі гри
screen.blit(background_image, (0, 0))

for coin in coins:
    screen.blit(coin_image, coin)

for acceleration in accelerations:
    screen.blit(acceleration_image, acceleration)

for deceleration in decelerations:
    screen.blit(deceleration_image, deceleration)

for enemy in enemies:
    enemy.move()
    enemy.draw(screen)

# Відображення ворогів (якщо є)
for enemy in enemies:
    screen.blit(enemy_image, enemy)

def check_colliding():
    global coin_count, acceleration_active, deceleration_active, speed_boost_time, speed_reduction_time
    coll = [False, False]
    rstrt = False
    screen.blit(font.render(f'Coin Count: {int(coin_count)} ', True, 'white'), (10, 40))

    for coin in coins[:]:
        if abs(coin[0] - player.centerx) < 25 and abs(coin[1] - player.centery) < 25:
            coins.remove(coin)
            coin_count += 1  # Збільшуємо лічильник монеток на 1
        
    for acceleration in accelerations[:]:
        if abs(acceleration[0] - player.centerx) < 25 and abs(acceleration[1] - player.centery) < 25:
            accelerations.remove(acceleration)
            acceleration_active = True
            speed_boost_time = pygame.time.get_ticks()

    for deceleration in decelerations[:]:
        if abs(deceleration[0] - player.centerx) < 25 and abs(deceleration[1] - player.centery) < 25:
            decelerations.remove(deceleration)
            deceleration_active = True
            speed_reduction_time = pygame.time.get_ticks()

    for enemy in enemies[:]:
        enemy_rect = pygame.Rect(int(enemy[0]), int(enemy[1]), enemy_image.get_width(), enemy_image.get_height())
        if player.colliderect(enemy_rect):
            if coin_count > 0:  # Перевірка, щоб кількість монет не стала від'ємною
                coin_count -= 1  # Віднімаємо одну монету
            enemies.remove(enemy)  # Видаляємо ворога після зіткнення

    if player.colliderect(bot_plat):
        coll[0] = True
    elif player.colliderect(top_plat):
        coll[1] = True

    if laser_line.colliderect(player):
        rstrt = True

    if rocket_active:
        if rocket.colliderect(player):
            rstrt = True

    return coll, rstrt


def generate_laser():
    laser_type = random.randint(0, 1)
    offset = random.randint(10, 300)
    if laser_type == 0:
        laser_width = random.randint(100, 300)
        laser_y = random.randint(100, HEIGHT - 100)
        new_lase = [[WIDTH + offset, laser_y], [WIDTH + offset + laser_width, laser_y]]
    else:
        laser_height = random.randint(100, 300)
        laser_y = random.randint(100, HEIGHT - 400)
        new_lase = [[WIDTH + offset, laser_y], [WIDTH + offset, laser_y + laser_height]]
    return new_lase


def draw_rocket(coords, mode):
    if mode == 0:
        rock = pygame.draw.rect(screen, 'dark red', [coords[0] - 60, coords[1] - 25, 50, 50], 0, 5)
        screen.blit(font.render('!', True, 'black'), (coords[0] - 40, coords[1] - 20))
        if not pause:
            if coords[1] > player_y + 10:
                coords[1] -= 3
            else:
                coords[1] += 3
    else:
        rock = pygame.draw.rect(screen, 'red', [coords[0], coords[1] - 10, 50, 20], 0, 5)
        pygame.draw.ellipse(screen, 'orange', [coords[0] + 50, coords[1] - 10, 50, 20], 7)
        if not pause:
            coords[0] -= 10 + game_speed

    return coords, rock


def draw_pause():
    pygame.draw.rect(surface, (128, 128, 128, 150), [0, 0, WIDTH, HEIGHT])
    pygame.draw.rect(surface, 'dark gray', [200, 150, 600, 50], 0, 10)
    surface.blit(font.render('Game Paused. Escape Btn Resumes', True, 'black'), (220, 160))
    restart_btn = pygame.draw.rect(surface, 'white', [200, 220, 280, 50], 0, 10)
    surface.blit(font.render('Restart', True, 'black'), (220, 230))
    quit_btn = pygame.draw.rect(surface, 'white', [520, 220, 280, 50], 0, 10)
    surface.blit(font.render('Quit', True, 'black'), (540, 230))
    pygame.draw.rect(surface, 'dark gray', [200, 300, 600, 50], 0, 10)
    surface.blit(font.render(f'Lifetime Distance Ran: {int(lifetime)}', True, 'black'), (220, 310))
    screen.blit(surface, (0, 0))
    return restart_btn, quit_btn


def modify_player_info():
    global high_score, lifetime
    if distance > high_score:
        high_score = distance
    lifetime += distance
    with open('player_info.txt', 'w') as file:
        file.write(str(int(high_score)) + '\n')
        file.write(str(int(lifetime)))

run = True
while run:
    timer.tick(fps)
    if counter < 40:
        counter += 1
    else:
        counter = 0
    if not pause and random.randint(0, 100) < 3:
        coins.append(generate_coin())
        accelerations.append(generate_acceleration())
        decelerations.append(generate_deceleration())

    if acceleration_active:
        if pygame.time.get_ticks() - speed_boost_time <= 15000:  # 15 секунд
            game_speed *= 2
        else:
            acceleration_active = False

    if deceleration_active:
        if pygame.time.get_ticks() - speed_reduction_time <= 15000:  # 15 секунд
            game_speed /= 2
        else:
            deceleration_active = False

    if new_laser:
        laser = generate_laser()
        new_laser = False
    lines, top_plat, bot_plat, laser, laser_line = draw_screen(lines, laser)
    if pause:
        restart, quits = draw_pause()

    if not pause and random.randint(0, 100) < 3:
        enemies.append(generate_enemy())

    if not rocket_active and not pause:
        rocket_counter += 1
    if rocket_counter > 180:
        rocket_counter = 0
        rocket_active = True
        rocket_delay = 0
        rocket_coords = [WIDTH, HEIGHT/2]
    if rocket_active:
        if rocket_delay < 90:
            if not pause:
                rocket_delay += 1
            rocket_coords, rocket = draw_rocket(rocket_coords, 0)
        else:
            rocket_coords, rocket = draw_rocket(rocket_coords, 1)
        if rocket_coords[0] < -50:
            rocket_active = False

    player = draw_player()
    enemy = draw_enemy()
    colliding, restart_cmd = check_colliding()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            modify_player_info()
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.key == pygame.K_p:  # Натиснуто клавішу 'p'
                pause = not pause
            if event.key == pygame.K_ESCAPE:
                if pause:
                    pause = False
                else:
                    pause = True
            if event.key == pygame.K_SPACE and not pause:
                booster = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                booster = False
        if event.type == pygame.MOUSEBUTTONDOWN and pause:
            if restart.collidepoint(event.pos):
                restart_cmd = True
            if quits.collidepoint(event.pos):
                modify_player_info()
                run = False
    if pause:
        draw_pause()
    if not pause:
        distance += game_speed
    if booster:
        y_velocity -= gravity
    else:
        y_velocity += gravity
    if (colliding[0] and y_velocity > 0) or (colliding[1] and y_velocity < 0):
        y_velocity = 0
    player_y += y_velocity
    modify_player_info()  # Виклик функції збереження даних

    # progressive speed increases
    if distance < 50000:
        game_speed = 1 + (distance // 500) / 10
    else:
        game_speed = 11

    if laser[0][0] < 0 and laser[1][0] < 0:
        new_laser = True

    if distance - new_bg > 500:
        new_bg = distance
        bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if restart_cmd:
        modify_player_info()
        coin_count = 0 
        distance = 0
        rocket_active = False
        rocket_counter = 0
        pause = False
        player_y = init_y
        y_velocity = 0
        restart_cmd = 0
        new_laser = True

    if distance > high_score:
        high_score = int(distance)

    pygame.display.flip()
pygame.quit()