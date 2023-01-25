from constants import*
from classes.Sprite import*
from classes.Window import*
from classes.Player import*
from classes.Enemy import*
from classes.Wall import*
from functions import win_lose, draw_sprites

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_CAPTION, BACKGROUND_PATH)

player = Player(SPRITE_WIDTH, SPRITE_HEIGHT, PLAYER_PATH, PLAYER_X, PLAYER_Y, PLAYER_SPEED)
enemy = Enemy(SPRITE_WIDTH, SPRITE_HEIGHT, MONSTER_PATH, MONSTER_X, MONSTER_Y, MONSTER_SPEED)
goal = Sprite(SPRITE_WIDTH, SPRITE_HEIGHT, GOAL_PATH, GOAL_X, GOAL_Y, GOAL_SPEED)

wall1 = Wall(154, 205, 50, 100, 20, 450, 10)
wall2 = Wall(154, 205, 50, 100, 480, 350, 10)
wall3 = Wall(154, 205, 50, 100, 20, 10, 380)

pygame.mixer.music.load(MUSIC_PATH)
pygame.mixer.music.play()

game = True
finish = False

while game:

    if finish != True:
        draw_sprites(player, wall1, wall2, wall3, enemy, goal, window)
    
    player.control(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
    enemy.move()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    
    finish = win_lose(player, wall1, wall2, wall3, enemy, goal, window.display)

    pygame.display.flip()
    window.clock.tick(FPS)
    
