import pygame
import os

# Ініалізуємо всі методи модулю pygame
pygame.init()

#Базові налаштування об'єктів
class Settings():
    def __init__(self, 
                width = None, 
                height= None, 
                x= None, 
                y= None,
                bgcolor = None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.bgcolor = bgcolor


# Клас кнопки. Він має ті ж властивості, що і клас налаштування, проте додається
# прямокутник з текстом
class Button(Settings):
    def __init__(self, width, height, x, y, bgcolor, text):
        super().__init__(width, height, x, y, bgcolor)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.Font(None, self.height // 2)
        self.text = self.font.render(text, True, (0, 0, 0))

    def draw(self):
        self.rect.x = settings.width // 2 - self.width // 2
        self.rect.y = settings.height // 2 - self.height // 2
        pygame.draw.rect(window, self.bgcolor, self.rect)
        window.blit(self.text, (self.rect.x + 10, self.rect.y + 10))

# Об'єкт для налаштування вікна та інших об'єктів
settings = Settings(width=300, height=300, bgcolor=(125, 125, 125))

# Задаємо розмір вікна, заповнюємо його кольором та встановлюємо підпис вікна
window = pygame.display.set_mode((settings.width, settings.height))
window.fill(settings.bgcolor)
pygame.display.set_caption("Question-Answer")

# Створюємо об'єкт годинника для налаштування fps
clock = pygame.time.Clock()

# Створюємо першу кнопку, задаємо її розміри, координати та колір
button1 = Button(100, 50, 0, 0, (136, 4, 227), "Button1")

# Зміна для управління ігровим циклом. Показує, чи продовжується гра, чи вона закінчилась
game = True
 
# Ігровий цикл
while game:
 
    # Встановлюємо fps
    clock.tick(60)

    # Рендеремо кнопки
    button1.draw()

    # Беребераємо декілька важливих подій. На основі події робимо різні дії
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    # Оновлюємо, перемальовуємо або перендеруємо весь екран
    pygame.display.flip()

