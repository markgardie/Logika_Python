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
pause = False

# Створення персонажів і вікна
window_play = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, WHITE)
menu_window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, WHITE)
set_window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, WHITE)

player = Player(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_X, PLAYER_Y, PLAYER_PATH, PLAYER_SPEED)
lable = Sprite(LABLE_WIDTH, LABLE_HEIGHT, LABLE_X, LABLE_Y, LABLE_PATH, LABLE_SPEED)

play_button = Button(BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_X, PBUTTON_Y, PBUTTON_PATH, BUTTON_SPEED, pbutton_clicked)
set_button = Button(BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_X, SBUTTON_Y, SBUTTON_PATH, BUTTON_SPEED, sbutton_clicked)
exit_button = Button(BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_X, EBUTTON_Y, EBUTTON_PATH, BUTTON_SPEED, ebutton_clicked)
back_button = Button(BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_X, BBUTTON_Y, BBUTTON_PATH, BUTTON_SPEED, bbutton_clicked)

level = 1
# головний цикл
while game:
    # Перевірка закриття гри
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if level == 1:
        menu_window.screen.blit(play_button.image, (play_button.hitbox.x, play_button.hitbox.y))
        menu_window.screen.blit(set_button.image, (set_button.hitbox.x, set_button.hitbox.y))
        menu_window.screen.blit(exit_button.image, (exit_button.hitbox.x, exit_button.hitbox.y))

        # Обробка кліків миші
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()

                level = play_button.check_click(mouse_pos, level)
                level = set_button.check_click(mouse_pos, level)
                game = exit_button.check_click(mouse_pos, game)


    elif level == 2:
        # Перевірка фінішу
    
        if not finish:
            if not pause:

                # Малювання
                window_play.screen.blit(player.image, (player.hitbox.x, player.hitbox.y))
                # Контроль
                player.controls(pygame.K_UP)

                jump(player)

                move_obstacles(obstacles)
                create_obstacles(obstacles, timer)
                draw_obstacles(window_play.screen, obstacles)

                colisions(player, obstacles, finish)

                key_pressed = pygame.key.get_pressed()

                if key_pressed[K_ESCAPE]:

                        pause = True
            
            elif pause:
                print("11")
    
    elif level == 3:
        
        set_window.screen.blit(lable.image, (lable.hitbox.x, lable.hitbox.y))
        set_window.screen.blit(back_button.image, (back_button.hitbox.x, back_button.hitbox.y))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()

                level = back_button.check_click(mouse_pos, level)


         
    # Оновлення кадру
    pygame.display.flip()
    window_play.screen.fill(WHITE)
    window_play.clock.tick(60)

    menu_window.screen.fill(WHITE)
    menu_window.clock.tick(60)

    set_window.screen.fill(WHITE)
    set_window.clock.tick(60)