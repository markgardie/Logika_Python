from Window import*
from Sprite import*
from Player import*
from constants import*
from functions import create_enemies, win, collisions, lose

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BACKGROUND_IMAGE_PATH)

player = Player(PLAYER_WIDTH, PLAYER_HEIGHT, WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80, PLAYER_IMAGE_PATH, PLAYER_SPEED)
enemies = create_enemies()
bullets = pg.sprite.Group()

BACKGROUND_SOUND.play()

game = True
finish = False
text = ""

while game:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            FIRE_SOUND.play()
            player.fire(bullets)

    if not finish:


        window.screen.blit(window.bg_image, (0, 0))
        window.screen.blit(player.image, (player.rect.x, player.rect.y))
        enemies.draw(window.screen)
        bullets.draw(window.screen)

        miss_text = FONT.render(f"{MISS_TEXT} {miss[0]}", True, TEXT_COLOR)
        scores_text = FONT.render(f"{SCORES_TEXT} {scores[0]}", True, TEXT_COLOR)

        window.screen.blit(miss_text, MISS_TEXT_COR)
        window.screen.blit(scores_text, SCORES_TEXT_COR)

        player.control(pg.K_a, pg.K_d)
        enemies.update()
        bullets.update()

        collisions(enemies, bullets)
        finish, text = win(finish, text)
        finish, text = lose(finish, text)
    else:
        window.screen.blit(window.bg_image, (0, 0))
        window.screen.blit(text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        BACKGROUND_SOUND.stop()

    pg.display.update()
    window.clock.tick(FPS)