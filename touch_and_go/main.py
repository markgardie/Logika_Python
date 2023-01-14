from classes.Sprite import*
from classes.Window import*
from constants import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_CAPTION, BACKGROUND_PATH)
sprite1 = Sprite(SPRITE_WIDTH, SPRITE_HEIGHT, SPRITE1_PATH, SPRITE1_X, SPRITE1_Y, SPEED)
sprite2 = Sprite(SPRITE_WIDTH, SPRITE_HEIGHT, SPRITE2_PATH, SPRITE2_X, SPRITE2_Y, SPEED)

game = True

while game: 

    window.display.blit(window.bg_image, (0, 0))
    window.display.blit(sprite1.image, (sprite1.x, sprite1.y))
    window.display.blit(sprite2.image, (sprite2.x, sprite2.y))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        
    
    window.display.flip()
    window.clock.tick(FPS)
    

