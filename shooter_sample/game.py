import pygame as pg
from random import randint

class Game():

    def create_objects(self):
       pass


    def draw_objects(self):
        pass

    def move_objects(self):

        pass

    def collisions(self):
        
        collides = pg.sprite.groupcollide(self.enemies, self.bullets, True, True)

        for c in collides:

            self.scores += 1

            x = randint(ENEMY_X_START, ENEMY_X_END)
            speed = randint(1, 5)

            enemy = Enemy(
                ENEMY_WIDTH, ENEMY_HEIGHT, 
                x, ENEMY_Y,
                ENEMY_IMAGE_PATH, speed
            )

            self.enemies.add(enemy)

    def win_lose(self):
       
        font = pg.font.Font(FONT_NAME, FONT_SIZE)


        if self.scores > GOAL:
           self.finish = True
           self.text = font.render(WIN_TEXT, True, BLACK)

        if self.miss > MAX_MISS:
            self.finish = True
            self.text = font.render(LOSE_TEXT, True, BLACK)

    
    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.player.fire(self.bullets)
        
    def update_window(self):
        self.window.clock.tick(FPS)
        pg.display.update()

    def game_loop(self):
        self.create_objects()
        self.game = True
        self.finish = False

        while self.game:
            if self.finish:
                self.window.screen.blit(self.text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
            else:
                self.draw_objects()
                self.move_objects()
                self.collisions()
                self.win_lose()
                self.update_window()

Game().game_loop()