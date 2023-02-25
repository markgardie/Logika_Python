from Enemy import*


def create_enemies():

    enemies = pygame.sprite.Group()

    for i in range(ENEMY_NUMBER):

        speed = randint(1, 5)
        x = randint(100, WINDOW_WIDTH - 100)

        enemy = Enemy(ENEMY_WIDTH, ENEMY_HEIGHT, x, ENEMY_Y,ENEMY_IMAGE_PATH, speed)

        enemies.add(enemy)

    return enemies