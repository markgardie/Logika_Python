import pygame as pg

 
pg.init()

# створюємо вікно
class Window():

    # конструктор
    # властивості: розміри, підпис вікна, шлях до фонового зображення
    def __init__(self, width, height, caption, background):

        # створюємо вікно
        self.screen = pg.display.set_mode((width, height))
        # задаємо підпис вікна
        pg.display.set_caption(caption)

        # завантажуємо зображення по шляху
        self.bg_image = pg.image.load(background)
        # змінюємо розмір зображення, аби воно збігалось з розмірами вікна
        self.bg_image = pg.transform.scale(self.bg_image, (width, height))

        # створюємо годинник
        # тіки годинника визначають час, коли треба оновити екран та кадри
        self.clock = pg.time.Clock()
    