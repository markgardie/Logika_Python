from constants import*
from classes.Sprite import*
from classes.Window import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_CAPTION, BACKGROUND_PATH)

sprite1 = Sprite(SPRITE_WIDTH, SPRITE_HEIGHT, SPRITE1_PATH, SPRITE1_X, SPRITE1_Y)
sprite2 = Sprite(SPRITE_WIDTH, SPRITE_HEIGHT, SPRITE2_PATH, SPRITE2_X, SPRITE2_Y)

game = True

while game:

    pygame.display.flip()
    window.clock.tick(FPS)

    window.display.blit(window.bg_image, (0,0))
    window.display.blit(sprite1.image, (sprite1.x, sprite1.y))
    window.display.blit(sprite2.image, (sprite2.x, sprite2.y))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    sprite1.control(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
    sprite2.control(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
