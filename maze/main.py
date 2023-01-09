from constants import*
from classes.Sprite import*
from classes.Window import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_CAPTION, BACKGROUND_PATH)

player = Sprite(SPRITE_WIDTH, SPRITE_HEIGHT, PLAYER_PATH, PLAYER_X, PLAYER_Y, PLAYER_SPEED)
monster = Sprite(SPRITE_WIDTH, SPRITE_HEIGHT, MONSTER_PATH, MONSTER_X, MONSTER_Y, MONSTER_SPEED)
goal = Sprite(SPRITE_WIDTH, SPRITE_HEIGHT, GOAL_PATH, GOAL_X, GOAL_Y, GOAL_SPEED)

pygame.mixer.music.load(MUSIC_PATH)
pygame.mixer.music.play()

game = True

while game:

    pygame.display.flip()
    window.clock.tick(FPS)

    window.display.blit(window.bg_image, (0,0))
    window.display.blit(player.image, (player.x, player.y))
    window.display.blit(monster.image, (monster.x, monster.y))
    window.display.blit(goal.image, (goal.x, goal.y))


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    
