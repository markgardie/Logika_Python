import random
import pygame
import os

pygame.init()

WIDTH = 1000
HEIGHT = 600
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

pygame.mixer.init()
asitwas = pygame.mixer.Sound('sound/Harry Styles - As It Was.mp3')
asitwas.set_volume(0.3)

asitwas.play()

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

# Завантаження шляхів до ресурсів
PROJECT_PATH = os.path.abspath(__file__ + "/..")
PLAY_PATH = os.path.join(PROJECT_PATH, "play")
COIN_IMAGE_PATH = os.path.join(PLAY_PATH, "coin.png")
PLAYER_IMAGE_PATH = os.path.join(PLAY_PATH, "player.png")
ENEMY_IMAGE_PATH = os.path.join(PLAY_PATH, "enemy.png")
BACKGROUND_IMAGE_PATH = os.path.join(PLAY_PATH, "background.png")
BOOSTED_IMAGE_PATH = os.path.join(PLAY_PATH, "boosted.png")
ACCELERATION_IMAGE_PATH = os.path.join(PLAY_PATH, "acceleration.png")
DECELERATION_IMAGE_PATH = os.path.join(PLAY_PATH, "deceleration.png")

background_image = pygame.image.load(BACKGROUND_IMAGE_PATH).convert()
player_image = pygame.image.load(PLAYER_IMAGE_PATH).convert()
boosted_image = pygame.image.load(BOOSTED_IMAGE_PATH).convert()
coin_image = pygame.image.load(COIN_IMAGE_PATH).convert()
enemy_image = pygame.image.load(ENEMY_IMAGE_PATH).convert()
acceleration_image = pygame.image.load(ACCELERATION_IMAGE_PATH).convert()
deceleration_image = pygame.image.load(DECELERATION_IMAGE_PATH).convert()

class Acceleration(pygame.sprite.Sprite):
    def __init__(self, acceleration_rate, game_speed):
        self.acceleration_rate = acceleration_rate
        self.speed = game_speed

    def apply(self, speed):
        """Збільшує швидкість гравця вдвічі."""
        return speed * 2  # Збільшення швидкості вдвічіclass AccelerationSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, game_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(ACCELERATION_IMAGE_PATH).convert_alpha(), (50, 50))
        self.rect = self.image.get_rect(center=(WIDTH + 100, random.randint(50, HEIGHT - 50)))
        self.speed = game_speed

    def update(self):
        # self.rect.x -= self.speed  # Закоментуйте або видаліть цей рядок
        if self.rect.right < 0:
            self.kill()

class Deceleration(pygame.sprite.Sprite):
    def __init__(self, deceleleration_rate, game_speed):
        self.deceleration_rate = deceleleration_rate
        self.speed = game_speed

    def apply(self, speed):
        """Зменшує швидкість гравця вдвічі."""
        return speed / 2  # Збільшення швидкості вдвічіclass AccelerationSprite(pygame.sprite.Sprite):
    
    def __init__(self, image_path, game_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(DECELERATION_IMAGE_PATH).convert_alpha(), (50, 50))
        self.rect = self.image.get_rect(center=(WIDTH + 100, random.randint(50, HEIGHT - 50)))
        self.speed = game_speed

    def update(self):
        if self.rect.right < 0:
            self.kill()

# Приклад використання класів
acceleration = Acceleration(0.1, 3)
deceleration = Deceleration(0.1, 3)

current_speed = 1.0  # Початкова швидкість гравця
current_speed = acceleration.apply(current_speed)  # Прискорення гравця
current_speed = deceleration.apply(current_speed)  # Зменшення швидкості гравця


# Клас для ворога
class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_path, line, game_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_path).convert(), (130, 56))
        self.rect = self.image.get_rect(center=(WIDTH + 100, lines[line]))
        self.speed = game_speed

    def update(self):
        if self.rect.right < 0:  # Якщо ворог вийшов за межі екрану, видаляємо його
            self.kill()

def generate_acceleration():
    # Створення об'єкта прискорення
    return Acceleration(ACCELERATION_IMAGE_PATH, game_speed)

def generate_deceleration():
    # Створення об'єкта зменшення швидкості
    return Deceleration(DECELERATION_IMAGE_PATH, game_speed)

# Функції для генерації об'єктів
def generate_enemy():
    # Генерація ворога
    line = random.choice([0, 1, 2, 3])  # Вибір лінії для руху ворога
    return Enemy(ENEMY_IMAGE_PATH, line, game_speed)

def generate_coin():
    x = WIDTH + 100
    y = random.randint(100, HEIGHT - 100)
    return [x, y]

all_enemies = pygame.sprite.Group()
all_accelerations = pygame.sprite.Group()
all_decelerations = pygame.sprite.Group()

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
        pygame.draw.circle(screen, 'gold', coin, 10)

    lase_line = pygame.draw.line(screen, 'yellow', (lase[0][0], lase[0][1]), (lase[1][0], lase[1][1]), 10)
    pygame.draw.circle(screen, 'yellow', (lase[0][0], lase[0][1]), 12)
    pygame.draw.circle(screen, 'yellow', (lase[1][0], lase[1][1]), 12)
    screen.blit(font.render(f'Distance: {int(distance)} m', True, 'white'), (10, 10))
    screen.blit(font.render(f'High Score: {int(high_score)} m', True, 'white'), (10, 70))
    return line_list, top, bot, lase, lase_line


# draw player including animated states
def draw_player():
    play = pygame.rect.Rect((120, player_y + 10), (25, 60))
    # pygame.draw.rect(screen, 'green', play, 5)
    if player_y < init_y or pause:
        if booster:
            pygame.draw.ellipse(screen, 'red', [100, player_y + 50, 20, 30])
            pygame.draw.ellipse(screen, 'orange', [105, player_y + 50, 10, 30])
            pygame.draw.ellipse(screen, 'yellow', [110, player_y + 50, 5, 30])
        pygame.draw.rect(screen, 'yellow', [128, player_y + 60, 10, 20], 0, 3)
        pygame.draw.rect(screen, 'orange', [130, player_y + 60, 10, 20], 0, 3)
    else:
        if counter < 10:
            pygame.draw.line(screen, 'yellow', (128, player_y + 60), (140, player_y + 80), 10)
            pygame.draw.line(screen, 'orange', (130, player_y + 60), (120, player_y + 80), 10)
        elif 10 <= counter < 20:
            pygame.draw.rect(screen, 'yellow', [128, player_y + 60, 10, 20], 0, 3)
            pygame.draw.rect(screen, 'orange', [130, player_y + 60, 10, 20], 0, 3)
        elif 20 <= counter < 30:
            pygame.draw.line(screen, 'yellow', (128, player_y + 60), (120, player_y + 80), 10)
            pygame.draw.line(screen, 'orange', (130, player_y + 60), (140, player_y + 80), 10)
        else:
            pygame.draw.rect(screen, 'yellow', [128, player_y + 60, 10, 20], 0, 3)
            pygame.draw.rect(screen, 'orange', [130, player_y + 60, 10, 20], 0, 3)
    # jetpack, body and head
    pygame.draw.rect(screen, 'white', [100, player_y + 20, 20, 30], 0, 5)
    pygame.draw.ellipse(screen, 'orange', [120, player_y + 20, 30, 50])
    pygame.draw.circle(screen, 'orange', (135, player_y + 15), 10)
    pygame.draw.circle(screen, 'black', (138, player_y + 12), 3)
    return play

def check_colliding():
    global coin_count
    coll = [False, False]
    rstrt = False
    screen.blit(font.render(f'Coin Count: {int(coin_count)} ', True, 'white'), (10, 40))

    for coin in coins[:]:
        if abs(coin[0] - player.centerx) < 25 and abs(coin[1] - player.centery) < 25:
            coins.remove(coin)
            coin_count += 1  # Збільшуємо лічильник монеток на 1

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
    
    # Оновлення кнопки restart
    restart_btn = pygame.draw.rect(surface, 'white', [200, 220, 280, 50], 0, 10)
    surface.blit(font.render('Restart', True, 'black'), (restart_btn.x + 20, restart_btn.y + 10))
    
    # Оновлення кнопки quit
    quit_btn = pygame.draw.rect(surface, 'white', [520, 220, 280, 50], 0, 10)
    surface.blit(font.render('Quit', True, 'black'), (quit_btn.x + 20, quit_btn.y + 10))
    
    # Створення кнопки continue
    proceed_btn = pygame.draw.rect(surface, 'white', [200, 300, 280, 50], 0, 10)
    surface.blit(font.render('Continue', True, 'black'), (proceed_btn.x + 20, proceed_btn.y + 10))
    
    screen.blit(surface, (0, 0))
    return restart_btn, quit_btn, proceed_btn


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

    # Зменшення частоти генерації
    if random.randint(0, 100) < 0.5:  # Зменшення шансу з 5% до 0.2%
        all_accelerations.add(generate_acceleration())

    if random.randint(0, 100) < 0.5:  # Зменшення шансу з 5% до 0.2%
        all_decelerations.add(generate_deceleration())

    if new_laser:
        laser = generate_laser()
        new_laser = False
    lines, top_plat, bot_plat, laser, laser_line = draw_screen(lines, laser)
    if pause:
        restart, quits, proceed_btn = draw_pause()

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

    # Оновлення всіх спрайтів
    all_enemies.update()
    all_accelerations.update()
    all_decelerations.update()

    # Відображення всіх спрайтів
    all_enemies.draw(screen)
    all_accelerations.draw(screen)
    all_decelerations.draw(screen)
    player = draw_player()
    colliding, restart_cmd = check_colliding()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            modify_player_info()
            run = False
        
        if event.type == pygame.KEYDOWN:
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
            mouse_x, mouse_y = event.pos
            if restart.collidepoint(mouse_x, mouse_y):
                restart_game()  # Виклик функції перезапуску гри
            elif proceed_btn.collidepoint(mouse_x, mouse_y):
                pause = False
            elif quits.collidepoint(mouse_x, mouse_y):
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

    if random.randint(0, 100) < 5:  # Шанс створення ворога 5%
        all_enemies.add(generate_enemy())

    

    def restart_game():
        global coin_count, distance, rocket_active, rocket_counter, pause, player_y, y_velocity, new_laser, high_score
        coin_count = 0 
        distance = 0
        rocket_active = False
        rocket_counter = 0
        pause = False
        player_y = init_y
        y_velocity = 0
        new_laser = True
        high_score = 0 

    
    if restart_cmd:
        restart_game()

    if distance > high_score:
        high_score = int(distance)

    pygame.display.flip()
pygame.quit()