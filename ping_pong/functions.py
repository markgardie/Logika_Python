from random import randint

def collisions(ball, platform1, platform2):

    if ball.rect.colliderect(platform1.rect):
        direction_x = 1
        direction_y = randint(-1, 1)