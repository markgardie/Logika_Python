import pygame as pg
from Sprite import Sprite
from Window import Window
from Player import Player
from Enemy import Enemy
from Constants import *
from random import randint

class Game():

    # створення об'єктів гри
    def create_objects(self):
        
        # основні персонажі
        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BACKGROUND_IMAGE_PATH)
        self.player = Player(PLAYER_WIDTH, PLAYER_HEIGHT,
                             PLAYER_X, PLAYER_Y,
                             PLAYER_IMAGE_PATH, PLAYER_SPEED)
        self.bullets = pg.sprite.Group()
        self.create_enemies()

        # лічильники
        self.miss = 0
        self.scores = 0

        self.create_counters()

        # нюанси: навіщо треба група
        # вона треба для запуску руху, малювання та інших дій для 
        # декількох спрайтів одночасно (наприклад, відразу всі вороги рухаються)

    # створення текстів лічильників
    def create_counters(self):
        self.scores_text = FONT.render(f"{SCORES_TEXT} {self.scores}", True, BLACK)
        self.miss_text = FONT.render(f"{MISS_TEXT} {self.miss}", True, BLACK)

        # нюанси: f-строка
        # дозволяє вставляти в строку тексту дані, які змінюються (змінна)
        # в нашому випадку бали в лічильнику постійно змінюються, тому
        # ми підставляємо змінні scores, miss

    # створення ворогів
    def create_enemies(self):
        
        # створюємо групу ворогів
        self.enemies = pg.sprite.Group()

        # циклом генеруємо відповідну кількість ворогів
        for i in range(ENEMY_NUMBER):
            self.generate_enemy()

    # малювання об'єктів
    def draw_objects(self):
        # малювання одиночних об'єктів
        self.window.screen.blit(self.window.image, (0, 0))
        self.window.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
       
        # малювання текстів лічильників
        self.window.screen.blit(self.scores_text, SCORES_TEXT_COR)
        self.window.screen.blit(self.miss_text, MISS_TEXT_COR)

        # малювання груп спрайтів
        self.enemies.draw(self.window.screen)
        self.bullets.draw(self.window.screen)

        # нюанси: для малювання одиночних об'єктів використовуємо blit
        # а для групи - draw
        # картинку вікна ми малюємо в координатах 0,0, вгорі зліва, оскільки це 
        # початок вікна і початок картинки (вони таким чином зуміщуються)


    # рух об'єктів
    def move_objects(self):
        # користувач керується клавішами
        self.player.controls(pg.K_a, pg.K_d, pg.K_w, pg.K_s)

        # групи рухаються автоматично
        self.enemies.update()
        self.bullets.update()

    # перевірка торкань, колізій спрайтів
    def collisions(self):
        
        # перевіряється торкання груп ворогів та куль
        # при торканні збільшується кількість балів
        collides = pg.sprite.groupcollide(self.enemies, self.bullets, True, True)
        for collide in collides:
            self.scores += 1
            self.generate_enemy()
          
        # торкання ворога і нижньої межі
        # торкання ворога і гравця
        # при даній колізії збільшується кількість пропущених ворогів
        for enemy in self.enemies:
            if (enemy.rect.y > WINDOW_HEIGHT - 5
                or enemy.rect.colliderect(self.player.rect)):
                self.miss += 1
                enemy.kill()
                self.generate_enemy()

        # нюанси: значення True в функції group означає
        # чи знищувати спрайти групи при торканні

    # генерація одного ворога
    def generate_enemy(self):

        # генерація випадкових характеристик: швидкості, х
        x = randint(ENEMY_X_START, ENEMY_X_END)
        speed = randint(1, 5)
        
        # створення ворога з випадковими характеристиками
        enemy = Enemy(ENEMY_WIDTH, ENEMY_HEGHT, 
                          x, ENEMY_Y,
                          ENEMY_IMAGE_PATH, speed)

        # додавання в групу
        self.enemies.add(enemy)

    # перевірка умов перемоги та поразки
    def win_lose(self):
        
        # виграємо, якщо досягли по балам певної цілі
        if self.scores >= GOAL:
            self.finish = True
            self.text = FONT.render(WIN_TEXT, True, BLACK)

        # програємо, якщо пропустили забагато ворогів
        if self.miss >= MAX_MISS:
            self.finish = True
            self.text = FONT.render(LOSE_TEXT, True, BLACK)

        # нюанси: що означає True в функції render
        # вказує на те, чи увімкнути згладжування, чи ні
        # розповісти про згладжування


    # перевірка подій
    def event_handler(self):
        for event in pg.event.get():
            # подія натискання на крестик
            # закриває вікно
            if event.type == pg.QUIT:
                self.game = False

            # подія натискання на пропуск
            # постріл
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.player.fire(self.bullets)

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
                self.event_handler()
                self.update_window()
            else:
                # перший, ігровий екран
                self.create_counters()
                self.draw_objects()
                self.move_objects()
                self.collisions()
                self.win_lose()
                self.update_window()
                self.event_handler()

Game().game_loop()