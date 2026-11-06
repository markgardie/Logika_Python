import pygame as pg
import constants as const

from ball import Ball
from player import Player
from label import Label
from sprite import Sprite


class Game:

    # Ініціалізація гри
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

    # Створення блоків
    def create_blocks(self):

        blocks = []

        for i in range(15):

            row = i // 5
            col = i % 5

            block = Sprite(
                (50 + col * 80, 20 + row * 40),
                (const.BLOCK_WIDTH, const.BLOCK_HEIGHT),
                0,
                const.BLOCK_IMAGE_PATH1
            )

            blocks.append(block)

        return blocks

    # Оновлення ігрових об'єктів
    def update(self):

        if self.scene != "playing":
            return

        # Рух платформи
        self.player.update(pg.K_LEFT, pg.K_RIGHT)

        # Збереження попередньої позиції м'яча
        self.previous_ball_rect = self.ball.rect.copy()

        # Рух м'яча
        self.ball.update()

        # Зіткнення зі стінами
        self.ball.collisions()

        # Інші зіткнення
        self.collisions()

        # Перевірка перемоги та програшу
        self.win_lose()

    # Відображення об'єктів
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

    # Перевірка перемоги та програшу
    def win_lose(self):

        if self.scene != "playing":
            return

        # Перемога — усі блоки знищені
        if len(self.blocks) == 0:

            self.scene = "win"

            self.end_label = Label(
                None,
                40,
                const.YELLOW,
                "Ви перемогли!"
            )

        # Програш — м'яч впав униз
        elif self.ball.rect.top >= const.WINDOW_HEIGHT:

            self.scene = "lose"

            self.end_label = Label(
                None,
                40,
                const.RED,
                "Ви програли!"
            )

    # Перевірка зіткнень
    def collisions(self):

        # Зіткнення м'яча з блоками
        for block in self.blocks[:]:

            if self.ball.rect.colliderect(block.rect):

                # Визначаємо напрямок відбиття
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

                # Видалення зруйнованого блоку
                self.blocks.remove(block)

                # Додавання очок
                self.score += 10

                # Оновлення рахунку
                self.score_label = Label(
                    None,
                    24,
                    const.WHITE,
                    f"Рахунок: {self.score}"
                )

                # За один кадр обробляємо лише один блок
                break

        # Зіткнення м'яча з платформою
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

    # Основний ігровий цикл
    def game_loop(self):

        while self.running:

            # Обробка подій
            for event in pg.event.get():

                if event.type == pg.QUIT:
                    self.running = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False

            # Оновлення гри
            self.update()

            # Малювання гри
            self.draw()

            pg.display.flip()

            # Обмеження FPS
            self.clock.tick(const.FPS)

        pg.quit()


# Запуск гри
if __name__ == "__main__":

    game = Game()
    game.game_loop()