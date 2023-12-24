import pygame as pg
from random import randint

class Game():

    def create_objects(self):
        self.enemies = pygame.sprite.Group()

    def create_enemy(self):
        x = randint(ENEMY_X_START, ENEMY_X_END)
        speed = randint(1, 5)

        enemy = Enemy(
                ENEMY_WIDTH, ENEMY_HEIGHT, 
                x, ENEMY_Y,
                ENEMY_IMAGE_PATH, speed
            )
        
        self.enemies.add(enemy)


    def draw_objects(self):
        # blit
        self.enemies.draw()

    def move_objects(self):
        # controls
        self.enemies.update()

    def collisions(self):
        
        collides = pg.sprite.groupcollide(self.bullets, self.enemies, True, True)

        for c in collides:
            self.scores += 1
            self.create_enemy()

        for enemy in self.enemies.sprites:
            if enemy.y > WINDOW_HEIGHT + 10 or enemy.rect.colliderect(self.player.rect):
                self.miss += 1
                enemy.kill()
                self.create_enemy()


    def win_lose(self):
       
        pass

    
    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game = False
            
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