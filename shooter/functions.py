from Enemy import*
from random import randint

def create_enemies():

    enemies = pygame.sprite.Group()

    for i in range(ENEMY_NUMBER):

        speed = randint(1, 5)
        x = randint(100, WINDOW_WIDTH - 100)

        enemy = Enemy(ENEMY_WIDTH, ENEMY_HEIGHT, x, ENEMY_Y,ENEMY_IMAGE_PATH, speed)

        enemies.add(enemy)

    return enemies

def collisions(enemies, bullets):

    collides = pygame.sprite.groupcollide(enemies, bullets, True, True)

    for collide in collides:
        
        scores[0] += 1

        x = randint(80, WINDOW_WIDTH - 80)
        speed = randint(1, 5)

        enemy = Enemy(ENEMY_WIDTH, ENEMY_HEIGHT, x, ENEMY_Y, ENEMY_IMAGE_PATH, speed)
        enemies.add(enemy)

def win(finish, text):


    if scores[0] >= 5:
        finish = True
        text = FONT.render(WIN_TEXT, True, TEXT_COLOR)

    return finish, text



def lose(finish, text):


    if miss[0] >= 5:
        finish = True
        text = FONT.render(LOSE_TEXT, True, TEXT_COLOR)

    return finish, text