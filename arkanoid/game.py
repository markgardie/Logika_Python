import pygame as pg
import constants as const
from ball import Ball
from player import Player
from label import Label
from sprite import Sprite

class Game:

    #dz: player, score_label, ball, window, clock, scene, score, blocks
    def __init__(self):
        pg.init()

        self.window = pg.display.set_mode(
            (const.WINDOW_WIDTH, const.WINDOW_HEIGHT)
        )

        pg.display.set_caption("Арканоїд")

        self.clock = pg.time.Clock()

        self.running = True
        self.scene = "playing"

        self.score = 0

        # Створення платформи
        self.player = Player(
            (
                (const.WINDOW_WIDTH - const.PLATFORM_WIDTH) // 2,
                const.WINDOW_HEIGHT - const.PLATFORM_HEIGHT - 20
            ),
            (const.PLATFORM_WIDTH, const.PLATFORM_HEIGHT),
            const.PLATFORM_SPEED,
            const.PLATFORM_IMAGE_PATH
        )

        # Створення м'яча
        self.ball = Ball(
            (
                self.player.rect.centerx - const.BALL_WIDTH // 2,
                self.player.rect.y - const.BALL_HEIGHT - 5
            ),
            (const.BALL_WIDTH, const.BALL_HEIGHT),
            const.BALL_SPEED,
            const.BALL_IMAGE_PATH
        )

        # Створення блоків
        self.blocks = self.create_blocks()

        # Напис із рахунком
        self.score_label = Label(
            None,
            24,
            const.WHITE,
            f"Рахунок: {self.score}"
        )

        self.end_label = None

        # Зберігаємо попередню позицію м'яча
        self.previous_ball_rect = self.ball.rect.copy()

    def create_blocks(self):
        blocks = []
        for i in range(15):
            row = i // 5
            col = i % 5

            block = Sprite(
                (50 + col*80, 20 + row*40),
                (const.BLOCK_WIDTH, const.BLOCK_HEIGHT),
                0,
                BLOCK_IMAGE_PATH1
            )

            blocks.append(block)

        return blocks
    
    #dz
    def update(self):
        pass

    #dz
    def draw(self):
        self.window.fill(const.BLACK)

        # Відображення блоків
        for block in self.blocks:
            block.draw(self.window)

        # Відображення платформи
        self.player.draw(self.window)

        # Відображення м'яча
        self.ball.draw(self.window)

        # Відображення рахунку
        self.score_label.draw(
            10,
            10,
            self.window
        )

        # Екран перемоги або програшу
        if self.end_label:

            x = (
                const.WINDOW_WIDTH -
                self.end_label.text_image.get_width()
            ) // 2

            y = const.WINDOW_HEIGHT // 2

            self.end_label.draw(
                x,
                y,
                self.window
            )

    def win_lose(self):
        pass

    def collisions(self):
        for block in self.blocks[:]:
            if block.rect.colliderect(self.ball.rect):
                if (
                    self.previous_ball_rect.bottom <= block.rect.top
                    or
                    self.previous_ball_rect.top >= block.rect.bottom
                ):

                    self.ball.dir_y *= -1

                    if self.previous_ball_rect.bottom <= block.rect.top:
                        self.ball.rect.bottom = block.rect.top
                    else:
                        self.ball.rect.top = block.rect.bottom

                else:

                    self.ball.dir_x *= -1

                    if self.previous_ball_rect.right <= block.rect.left:
                        self.ball.rect.right = block.rect.left
                    else:
                        self.ball.rect.left = block.rect.right

                self.blocks.remove(block)

                self.score += 10

                self.score_label = Label(
                    None,
                    24,
                    const.WHITE,
                    f"Score: {self.score}"
                )

                break

        
        if (
            self.ball.rect.colliderect(self.player.rect)
            and self.ball.dir_y > 0
        ):

            # Відбиваємо м'яч угору
            self.ball.rect.bottom = self.player.rect.top
            self.ball.dir_y = -1

            # Напрямок залежить від місця зіткнення
            hit_position = (
                self.ball.rect.centerx -
                self.player.rect.centerx
            )

            zone = self.player.rect.width / 6

            if hit_position < -zone:
                self.ball.dir_x = -1

            elif hit_position > zone:
                self.ball.dir_x = 1

            else:
                self.ball.dir_x = 0    

    def game_loop(self):
        pass
