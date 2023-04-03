import pygame

# ініціалізація (запуск) пайгейму
# треба для роботи шрифтів та текстів
pygame.init()

# вікно, базовий клас
# можна копіювати в різні проекти
class Window():

    # конструктор вікна
    # запускається під час створення нового вікна
    # задає початкові властивості
    # розміри, колір фону, надпис
    def __init__(self, width, height, bg_color, caption):

        # функція для створення вікна (екрану)
        self.screen = pygame.display.set_mode((width, height))
        # функція для створення надпису вікна
        pygame.display.set_caption(caption)
        # функція для заливки фона певним кольором
        self.screen.fill(bg_color)

        # годинник
        # в main він тікає і вказує, коли треба змінити кадри
        self.clock = pygame.time.Clock() 