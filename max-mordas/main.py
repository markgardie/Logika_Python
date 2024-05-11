from pygame import*
from constants import*
from functions import*
from player import*
from window import*
from button import*
from sprite import*

pygame.init()

# Змінні game і finish
game = True
finish = False

obstacles = []
timer = 0
level = 0
score = 0
score_timer = 0
coins_amount = 0
pause = False

# Створення персонажів і вікна
game_window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, WHITE)
menu_window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, WHITE)
set_window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, WHITE)
mark_window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, WHITE)

player = Player(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_X, PLAYER_Y, PLAYER_PATH, PLAYER_SPEED)
label = Sprite(LABEL_WIDTH, LABEL_HEIGHT, LABEL_X, LABEL_Y, LABEL_PATH, LABEL_SPEED)

coins_font = pygame.font.Font(None, COINS_FONT_SIZE)
loose_font = pygame.font.Font(None, LOOSE_FONT_SIZE)
score_font = pygame.font.Font(None, SCORE_FONT_SIZE)

play_button = Button(BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_X, PBUTTON_Y, PBUTTON_PATH, BUTTON_SPEED, pbutton_clicked)
set_button = Button(BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_X, SBUTTON_Y, SBUTTON_PATH, BUTTON_SPEED, sbutton_clicked)
exit_button = Button(BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_X, EBUTTON_Y, EBUTTON_PATH, BUTTON_SPEED, ebutton_clicked)
mark_button = Button(BUTTON_WIDTH, BUTTON_HEIGHT, MBUTTON_X, MBUTTON_Y, MBUTTON_PATH, BUTTON_SPEED, mbutton_clicked)
back_button = Button(BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_X, BBUTTON_Y, BBUTTON_PATH, BUTTON_SPEED, bbutton_clicked)

level = 2
# головний цикл
while game:

    mouse_pos = pygame.mouse.get_pos()

    # Перевірка закриття гри
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if level == 1:
                level = button_colisions(play_button, mouse_pos, level)
                level = button_colisions(set_button, mouse_pos, level)
                level = button_colisions(mark_button, mouse_pos, level)
                game = button_colisions(exit_button, mouse_pos, game)

            elif level == 2 and finish:

                level = button_colisions(back_button, mouse_pos, level)

            elif level == 2 and pause:

                level = button_colisions(back_button, mouse_pos, level)

            elif level == 3 or level == 4:

                level = button_colisions(back_button, mouse_pos, level)


    if level == 1:

        finish = False

        menu_window.screen.blit(play_button.image, (play_button.hitbox.x, play_button.hitbox.y))
        menu_window.screen.blit(set_button.image, (set_button.hitbox.x, set_button.hitbox.y))
        menu_window.screen.blit(exit_button.image, (exit_button.hitbox.x, exit_button.hitbox.y))
        menu_window.screen.blit(mark_button.image, (mark_button.hitbox.x, mark_button.hitbox.y))

        text = coins_font.render(str(coins_amount), True, BLACK)
        menu_window.screen.blit(text, (COINS_LABEL_X, COINS_LABEL_Y))

    elif level == 2:

        # Перевірка фінішу
    
        if not finish:
            if not pause:

                # Малювання
                game_window.screen.blit(player.image, (player.hitbox.x, player.hitbox.y))
                # Контроль
                player.controls(pygame.K_UP)

                jump(player)

                move_obstacles(obstacles)
                create_obstacles(obstacles, timer)
                draw_obstacles(game_window.screen, obstacles)

                finish = colisions(player, obstacles, finish)

                score, score_timer = score_adding(score, score_timer)

                key_pressed = pygame.key.get_pressed()

                text = score_font.render(str(score), True, BLACK)
                menu_window.screen.blit(text, (SCORE_LABEL_X, SCORE_LABEL_Y))

                if key_pressed[K_ESCAPE]:

                        pause = True
            
            elif pause:
                game_window.screen.blit(back_button.image, (back_button.hitbox.x, back_button.hitbox.y))
        elif finish:
            text = loose_font.render(LOOSE_TEXT, True, BLACK)
            game_window.screen.blit(text, (LOOSE_TEXT_X, LOOSE_TEXT_Y))

            game_window.screen.blit(back_button.image, (back_button.hitbox.x, back_button.hitbox.y))
    
    elif level == 3:
        
        set_window.screen.blit(label.image, (label.hitbox.x, label.hitbox.y))
        set_window.screen.blit(back_button.image, (back_button.hitbox.x, back_button.hitbox.y))


    elif level == 4:
        
        mark_window.screen.blit(back_button.image, (back_button.hitbox.x, back_button.hitbox.y))



         
    # Оновлення кадру
    pygame.display.flip()
    game_window.screen.fill(WHITE)
    game_window.clock.tick(60)

    menu_window.screen.fill(WHITE)
    menu_window.clock.tick(60)

    set_window.screen.fill(WHITE)
    set_window.clock.tick(60)