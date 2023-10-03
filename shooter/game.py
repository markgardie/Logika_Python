class Game():

    def create_objects(self):
       
       self.window = Window(
           WINDOW_WIDTH, WINDOW_HEIGHT,
           BACKGROUND_IMAGE_PATH, CAPTION
       )

       self.player = Player(
           PLAYER_WIDTH, PLAYER_HEIGHT,
           PLAYER_X, PLAYER_Y,
           PLAYER_IMAGE_PATH, PLAYER_SPEED
       )

       self.bullets = pg.sprite.Group()
       self.enemies = self.create_enemies()

       self.scores = 0
       self.miss = 0

    def create_enemies():
        enemies = pg.sprite.Group()

        for i in range(ENEMY_NUMBER):
            x = randint(80, WINDOW_WIDTH - 80)
            speed = randint(1, 5)

            enemy = Enemy(
                ENEMY_WIDTH, ENEMY_HEIGHT,
                x, ENEMY_Y, 
                ENEMY_IMAGE_PATH, speed
            )

            enemies.add(enemy)

        return enemies

    def draw_objects(self):
        pass

    def move_objects(self):

        pass

    def collisions(self):
        collides = pg.sprite.groupcollide(self.enemies, self.bullets, True, True)

        for c in collides:
            self.scores += 1
            
            x = randint(80, WINDOW_WIDTH - 80)
            speed = randint(1, 5)

            enemy = Enemy(
                ENEMY_WIDTH, ENEMY_HEIGHT,
                x, ENEMY_Y, 
                ENEMY_IMAGE_PATH, speed
            )

            enemies.add(enemy)

    def win_lose(self):
       pass
    
    def event_handler(self):
        pass
        
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