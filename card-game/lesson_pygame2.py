import pygame
import os
import random

pygame.init()

win_width = 845 # задаємо значення ширини вікна гри
win_height = 760 # задаємо значення висоти вікна гри

card_width = 200 # задаємо значення ширини спрайту карти
card_height = 320 # задаємо значення висоти спрайту карти

flag = 0 # змінна, яка відповідає за швидкість зміни анімації карти при натисканні на неї

FPS = 60 # швидкість зміни кадрів
# Словник картки бійця
dict_warrior = {
                    "HP": 9,
                    "Attack": 3,
                    "Defense": 5,
                    "Crystal": 5
                }
# Словник налаштувань 
dict_textSettings = {
                        "FONT_SIZE": 60,
                        "FONT_NAME": "font/dialog.otf",
                        "COLOR": (255,255,255)
                    }
#
# Створюємо вікно гри з конкретници параметрами ширини та висоти вікна гри
win = pygame.display.set_mode((win_width, win_height))
# Задаємо назву вікну гри
pygame.display.set_caption("Game Card")
# Знаходимо шлях до файлу-зображення icon 
path_image = os.path.join(os.path.abspath(__file__ + "/.."), "image/5.png")
# Завантажуємо зображення 
image1 = pygame.image.load(path_image)
# Задаємо зображення для вікна гри
pygame.display.set_icon(image1)
#________________________________________________________________________________________________#
class Card:
    def __init__(self, 
                    width= None, 
                    height= None, 
                    x= None, 
                    y= None, 
                    img= None,
                    #__________________ 
                    num_crystal= None, 
                    num_defense = None,
                    num_attack = None,
                    num_hp = None
                    #__________________
                ):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.NAME_IMG = img
        self.IMAGE = None # відповідає за збереження завантаженного зображення 
        self.NUMBER_CARD = None 
        self.RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT) # рект об'єкт картки
        self.KEY_PRESSED = False # відповідає за контроль, чи натиснута картка, True - натиснута
        self.IMPACT_TIME = 0 # відповідає за тривалість удару по супротивнику
        #___________________________ Завантажуємо шрифт, задаємо налаштування шрифту
        self.path_font = os.path.join(os.path.abspath(__file__ + '/..'), dict_textSettings["FONT_NAME"])
        self.main_font = pygame.font.Font(self.path_font, dict_textSettings["FONT_SIZE"])
        #___________________________ Задаємо об'єкти чисел на картці
        self.NUM_CRYSTAL = self.create_text(num_crystal)
        self.NUM_DEFENSE = self.create_text(num_defense)
        self.NUM_ATTACK = self.create_text(num_attack)
        self.NUM_HP = self.create_text(num_hp)
        #___________________________ Завантажуємо зображення до властивості self.IMAGE
        self.load_img()
    # Метод завантаження зображення з чіткими параметрами ширини та вистоти
    def load_img(self):
        path_image = os.path.join(os.path.abspath(__file__ + "/.."), self.NAME_IMG)
        self.IMAGE = pygame.image.load(path_image)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))
    # Метод створення текстових об'єктів 
    def create_text(self, dict_card):
        text = self.main_font.render(str(dict_card), True, dict_textSettings["COLOR"])
        return text    
    # Метод, що промальовує спрайти зображень, тексту
    def card_blit(self, win, enemy = None):
        win.blit(self.IMAGE, (self.X, self.Y))
        win.blit(self.NUM_CRYSTAL, (self.X + 12, self.Y + 5))
        win.blit(self.NUM_DEFENSE, (self.X + 12, self.Y + card_height - 65))
        win.blit(self.NUM_DEFENSE, (self.X + card_width - 35, self.Y + card_height - 65))
    
#________________________________________________________________________________________________#
# Список спрайтів коли кнопка не натиснута, повний розмір
list_sprite_UP = list()
# Список спрайтів  коли кнопка натиснута, розмір зображення на 10 пікселів меньший за основний із списка list_sprite1
list_sprite_DOWN = list()
#________________________________________________________________________________________________#
# функція що створює та додає спрайти до списків
def create_sprite(list_sprite, size = 0):
    x = 10
    # цикл, що ствоює кожне повторення новий об'єкт sprite та додає його до списку спрайтів
    for i in range(4):
        sprite = Card(
                        width= card_width - size,
                        height= card_height - size,
                        x= x,
                        y= win_height - card_height - 10,
                        img= "image/" + str(i+1) + ".png", #Приклад image/1.png після першого повторення циклу
                        num_crystal= dict_warrior["Crystal"],
                        num_defense= dict_warrior["Defense"],
                        num_hp= dict_warrior["HP"],
                        num_attack= dict_warrior["Attack"]
                    )
        # додаємо новий об'єкт до списку спрайтів
        list_sprite.append(sprite)        
        # задаємо порядковий номер для останнього доданого спрайта у список
        list_sprite[-1].NUMBER_CARD = i + 1
        # змінюємо координату х для переходу на 210 пікселів в праву сторону для створення наступної карти
        x += card_width + 10

#________________________________________________________________________________________________#
# застосовуємо метод та створюємо списки спрайтів
create_sprite(list_sprite_UP)
create_sprite(list_sprite_DOWN, size= 10)
#________________________________________________________________________________________________#
# основна функція гри 
def run_game():

    global flag # звертаємося до глобальної змінної вказанної на початку коду
    
    pressed_card_number = 0 # Змінна потрібна для фіксації чи натиснута картка чи ні
    # створюємо спайт ворога 
    sprite_enemy = Card(
        width=card_width + 40, 
        height=card_height + 30, 
        x = win_width//2 - card_width//2,
        y = win_height//2 - card_height,
        img="image/6.png"
        )

    frames = pygame.time.Clock()
   
    game = True
    while game:
        # Задаємо фон гри
        win.fill((128,0,255))
        # промальовуємо спрайт ворога
        win.blit(sprite_enemy.IMAGE, (sprite_enemy.X, sprite_enemy.Y))
        #
#________________________________________________________________________________________________#
        # Якщо значення змінної дорівнює 0, то на екрані відображаються основні спрайти
        if flag == 0:
            # Всі карти відображаються, якщо не натиснута карта супротивник
            for sprite in list_sprite_UP:
                sprite.card_blit(win)
        else:# інакше, значення змінної буде наближатися до 0, 
            # а в цей час, будуть відображатися основні спрайти, на екрані гри, крім того спрайту, 
            # на якого було таниснуто, для анімації натискання на картку
            flag -= 1 #
            for sprite in list_sprite_UP:
                if sprite.NUMBER_CARD != pressed_card_number:                   
                    sprite.card_blit(win)
#________________________________________________________________________________________________#
        # перевіряємо події чи є співпадіння 
        for event in pygame.event.get():
            # подія, якщо натиснути на хрестик вікна гри, припинити роботу циклу гри
            if event.type == pygame.QUIT:
                game = False
            # подія, якщо натиснуто колесо мищі, то друк координат, щоб знати точні координати де розміщувати майбутній об'єкт
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                print(event.pos)
            # подія, якщо ліву кнопку мищі болу натиснуто
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos # отримуємо координати кліку по ігровому екрану
                for el in list_sprite_UP:
                    # перевіряємо співпадіння координад, чи отримані координати співпали с діапазоном координатами
                    # Rect об'єкту карти на яку було натиснуто
                    if el.RECT.collidepoint(x, y) and sprite_enemy.IMPACT_TIME <= 0:
                        # Застереження від того, якщо користувач натисне на картку, але не вдарить супротивника, а знову вибире нову карту
                        for el1 in list_sprite_UP:
                            el1.KEY_PRESSED = False
                        print(f"Карта {el.NUMBER_CARD} нажата") # перевірка, яка карта була натиснута 
                        pressed_card_number = el.NUMBER_CARD # фіксує номер натиснутої карти до змінної
                        flag = 10
                        el.KEY_PRESSED = True # фіксуємо, що карта натиснута           
                # Подія натискання на карту супротивника
                if  sprite_enemy.RECT.collidepoint(x, y) and sprite_enemy.IMPACT_TIME <= 0:
                    sprite_enemy.KEY_PRESSED = True 
                    for el in list_sprite_UP:
                        # Якщо перед тим як натиснути на карту ворога, гравець натиснув на свою карту, 
                        # тілки тоді буде заданий таймер для переміщення карти гравця на карту супротивника 
                        if el.KEY_PRESSED:
                            sprite_enemy.IMPACT_TIME = 60
        # Робимо переміщення картки гравця до картки ворога, поки таймер не дорівнює 0
        if sprite_enemy.IMPACT_TIME > 0:
            list_sprite_UP[pressed_card_number - 1].KEY_PRESSED = False           
            list_sprite_UP[pressed_card_number - 1].X = sprite_enemy.X - 40
            list_sprite_UP[pressed_card_number - 1].Y = sprite_enemy.Y + 50            
            sprite_enemy.IMPACT_TIME -= 1
        # Знімаємо фіксацію натискання на карту супротивника, щоб  карта гравця перемістилася на своє місце
        if sprite_enemy.IMPACT_TIME <= 0:
            sprite_enemy.KEY_PRESSED = False
            list_sprite_UP[pressed_card_number - 1].X = list_sprite_UP[pressed_card_number - 1].RECT.x
            list_sprite_UP[pressed_card_number - 1].Y = list_sprite_UP[pressed_card_number - 1].RECT.y            
#________________________________________________________________________________________________#
        # Якщо значення змінної flag більше 0, 
        # то буде відображатись на екрані зменшений варіант спрайту, а точніше 10 повторень циклу гри, 
        # тому що змінна flag = 10
        if flag > 0:
            for el in list_sprite_DOWN:
                # змынюэться зображення тільки у тієї карти, яка була натиснута 
                if pressed_card_number == el.NUMBER_CARD:                    
                    el.card_blit(win)

        frames.tick(FPS) # частота зміни кадрів
        pygame.display.flip()# оновлюємо екран

run_game()