from constants import*
from classes.Sprite import*
from classes.Window import*
from classes.Player import*
from classes.Enemy import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_CAPTION, BACKGROUND_PATH)

player = Player(SPRITE_WIDTH, SPRITE_HEIGHT, PLAYER_PATH, PLAYER_X, PLAYER_Y, PLAYER_SPEED)
monster = Enemy(SPRITE_WIDTH, SPRITE_HEIGHT, MONSTER_PATH, MONSTER_X, MONSTER_Y, MONSTER_SPEED)
goal = Sprite(SPRITE_WIDTH, SPRITE_HEIGHT, GOAL_PATH, GOAL_X, GOAL_Y, GOAL_SPEED)

pygame.mixer.music.load(MUSIC_PATH)
pygame.mixer.music.play()

game = True

while game:

    window.display.blit(window.bg_image, (0,0))

    player.control(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
    monster.move()

    window.display.blit(player.image, (player.hitbox.x, player.hitbox.y))
    window.display.blit(monster.image, (monster.hitbox.x, monster.hitbox.y))
    window.display.blit(goal.image, (goal.hitbox.x, goal.hitbox.y))


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    
    pygame.display.flip()
    window.clock.tick(FPS)
    
