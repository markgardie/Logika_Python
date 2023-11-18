import pygame as pg
from Sprite import Sprite
from Window import Window
from Player import Player
from Enemy import Enemy
from Constants import *
from Wall import Wall

class Game():

    # створення об'єктів гри
    def create_objects(self):

        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_CAPTION, BACKGROUND_PATH)

        self.player = Player(SPRITE_WIDTH, SPRITE_HEIGHT,
                             PLAYER_X, PLAYER_Y,
                             PLAYER_PATH, PLAYER_SPEED)
        
        self.goal = Sprite(SPRITE_WIDTH, SPRITE_HEIGHT,
                           GOAL_X, GOAL_Y,
                           GOAL_PATH, GOAL_SPEED)
        
        self.enemy = Enemy(SPRITE_WIDTH, SPRITE_HEIGHT,
                           MONSTER_X, MONSTER_Y,
                           MONSTER_PATH, MONSTER_SPEED)
        
        self.wall1 = Wall(WALL_COLOR1, WALL_COLOR2, WALL_COLOR3, 
                          WALL_X, WALL1_Y, 
                          WALL1_WIDTH, WALL1_HEIGHT
                          )
        
        self.wall2 = Wall(WALL_COLOR1, WALL_COLOR2, WALL_COLOR3, 
                          WALL_X, WALL2_Y, 
                          WALL2_WIDTH, WALL2_HEIGHT
                          )
        
        self.wall3 = Wall(WALL_COLOR1, WALL_COLOR2, WALL_COLOR3, 
                          WALL_X, WALL3_Y, 
                          WALL3_WIDTH, WALL3_HEIGHT
                          )
        
        self.wall4 = Wall(WALL_COLOR1, WALL_COLOR2, WALL_COLOR3, 
                          WALL4_X, WALL4_Y, 
                          WALL4_WIDTH, WALL4_HEIGHT
                          )
        
        self.wall5 = Wall(WALL_COLOR1, WALL_COLOR2, WALL_COLOR3, 
                          WALL5_X, WALL5_Y, 
                          WALL5_WIDTH, WALL5_HEIGHT
                          )
        
        self.wall6 = Wall(WALL_COLOR1, WALL_COLOR2, WALL_COLOR3, 
                          WALL6_X, WALL6_Y, 
                          WALL6_WIDTH, WALL6_HEIGHT
                          )


    # малювання об'єктів
    def draw_objects(self):
        # малювання одиночних об'єктів
        self.window.screen.blit(self.window.image, (0, 0))
        self.window.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        self.window.screen.blit(self.goal.image, (self.goal.rect.x, self.goal.rect.y))
        self.window.screen.blit(self.enemy.image, (self.enemy.rect.x, self.enemy.rect.y))
        self.window.screen.blit(self.wall1.image, (self.wall1.rect.x, self.wall1.rect.y))
        self.window.screen.blit(self.wall2.image, (self.wall2.rect.x, self.wall2.rect.y))
        self.window.screen.blit(self.wall3.image, (self.wall3.rect.x, self.wall3.rect.y))
        self.window.screen.blit(self.wall4.image, (self.wall4.rect.x, self.wall4.rect.y))
        self.window.screen.blit(self.wall5.image, (self.wall5.rect.x, self.wall5.rect.y))
        self.window.screen.blit(self.wall6.image, (self.wall6.rect.x, self.wall6.rect.y))

        # нюанси: для малювання одиночних об'єктів використовуємо blit
        # а для групи - draw
        # картинку вікна ми малюємо в координатах 0,0, вгорі зліва, оскільки це 
        # початок вікна і початок картинки (вони таким чином зуміщуються)
        # треба також згадати, що малюється у нас зображення спрайту, а хітбокс
        # залишається невидимим

    # рух об'єктів
    def move_objects(self):
        # користувач керується клавішами
        self.player.controls(pg.K_a, pg.K_d, pg.K_w, pg.K_s)
        # ворог рухається автоматично
        self.enemy.move()

    # перевірка умов перемоги та поразки
    def win_lose(self):

        # створення шрифта
        font = pg.font.Font(None, FONT_SIZE)

        # умова поразки: коли гравець торкається ворога чи будь-якої стінки
        if (self.player.rect.colliderect(self.enemy.rect)
        or self.player.rect.colliderect(self.wall1.rect)
        or self.player.rect.colliderect(self.wall2.rect)
        or self.player.rect.colliderect(self.wall3.rect)):
            self.finish = True
            self.text = font.render(LOSE_TEXT, True, BLACK)
        
        # умова перемоги: коли гравець торкається скарбів (цілі)
        if self.player.rect.colliderect(self.goal.rect):
            self.finish = True
            self.text = font.render(WIN_TEXT, True, BLACK)

        # нюанси: що означає True в функції render
        # вказує на те, чи увімкнути згладжування, чи ні
        # розповісти про згладжування

    # оновлення вікна
    def update_window(self):
        # тік вказує, коли треба оновити кадри
        self.window.clock.tick(FPS)
        pg.display.update()

        # нюанси: є 2 функції оновлення: update, flip
        # update - оновлює тільки частину екрану, де були зміни
        # flip - оновлює весь екран
        # плюси update - економний (не треба весь екран перемальовувати)
        # мінуси update - можуть бути візуальні баги
        # плюси flip - відсутність багів при малюванні
        # мінуси flip - неекономний

    # перевірка подій
    def event_handler(self):
        for event in pg.event.get():
            # подія натискання на крестик
            # закриває вікно
            if event.type == pg.QUIT:
                self.game = False

    # ігровий цикл
    # повторює основні дії в грі, поки вона не закінчиться
    def game_loop(self):
        self.create_objects()

        # відповідає за закриття вікна
        self.game = True

        # відповідає за перемикання на фінальний екран
        self.finish = False

        while self.game:
            if self.finish:
                # фінальний екран
                self.window.screen.blit(self.text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
                self.update_window()
                self.event_handler()
            else:
                # перший, ігровий екран
                self.draw_objects()
                self.move_objects()
                self.win_lose()
                self.update_window()
                self.event_handler()

Game().game_loop()