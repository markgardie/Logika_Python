import pygame
 # Створює клас в pygame
pygame.init()
#Створює сам клас
class Window():

    # Конструктор
    def __init__(self, width, height, caption, background):

        # Створює вікно
        self.screen = pygame.display.set_mode((width, height))
        # Встановлює напис для вікна
        pygame.display.set_caption(caption)
        # Заливає вікно (або задній фон) одним кольором
        self.screen.fill(background)
        # Встановлює частоту кадрів
        self.clock = pygame.time.Clock()