from Enemy import*

def create_enemies():

    enemies = pg.sprite.Group()

    for i in range(ENEMY_NUMBER):
        
        x = randint(80, WINDOW_WIDTH - 80)
        speed = randint(1, 5)

        enemy = Enemy(ENEMY_WIDTH, ENEMY_HEGHT, x, ENEMY_Y, ENEMY_IMAGE_PATH, speed)

        enemies.add(enemy)

    return enemies