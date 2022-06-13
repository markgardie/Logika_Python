import pygame # для создание игры
import random # случайные числа
import time # время работы нашей программы 
import os # для работы с системой

pygame.font.init()
pygame.init()

display_width = 800 # ширина дисплея
display_height = 600 # высота дисплея

FPS = pygame.time.Clock()

# создаем класс спрайтов, где задаются все стандартные настройки всех спрайтов 
class Sprite_Game:
    # метод конструктор для задания свойств или полей нашего класса 
    def __init__(self, width, height, name_image, x, y, speed = 0, speed_X = 0):
        self.WIDTH = width # ширина спрайта
        self.HEIGHT = height #
        self.NAME_IMAGE = name_image # задаем название картинки для того чтобы потом ее загрузить
        self.X = x # 
        self.Y = y # 
        self.SPEED = speed # скорость движения спрайта в игре
        self.SPEED_X = speed_X
        self.END_IMAGE = "" # сорханям конечный результат картинкы для дальнейшей комфортной работы с этой картинкой
        self.WIN = 0
        self.RECT = pygame.Rect(x,y, width, height) # отвечает за взаимодействие объектов    
    # метод находит апсолютный путь к картинке по ее названию и загружает ее под размеры спрайта
    def load_image(self): 
        # объект отвечает за получение абсолютного пути к картинке 
        path_image = os.path.join(os.path.abspath(__file__ + "/.."), self.NAME_IMAGE) 
        # в объекте сохраняем картинку по абсолютному пути
        image1 = pygame.image.load(path_image)
        # трансформируем под размер спрайта и сохраняем в свойстве END_IMAGE
        self.END_IMAGE = pygame.transform.scale(image1, (self.WIDTH, self.HEIGHT))
# Задает структуру расположения объектов на ингровой карте
list_map = [
                "1111111111",
                "0001111000",
                "1111111111",
                "0001111000"
            ]
# для хранения всех созданных спайтов блоков 
list_block = list()
# перебор списка карты и создание объектов спрайтов блоков и загрузка картинки блока в проект 
def draw_block():
    x = 20 # начальные координаты превой платформы по Х
    y = 20 # начальные координаты превой платформы по У
    for string in list_map: # перебор значений списка list_map
        for pl in string: # перебор посимвольно строки 
            if pl == "1": # если в строке есть 1 то рисуем блок
                platform = Sprite_Game(70, 30, "image/3.png", x, y)
                platform.load_image()
                list_block.append(platform) # наполняем список платформами
            x += 76 # для отступа между платформами по горизонту
        y += 56 # для отступа между платформами по вертикали
        x = 20 # возвращаемся в начало строки перед началом рисования следующего ряда платформ
        
# отвечает за запуск игры
def start_game():
    move_right = False # запрет движения вправо
    move_left = False # запрет движения влево

    move_UP_DOWN = False # запрет движения вниз

    draw_block() # создает наши платформы 
    #
    screen = pygame.display.set_mode((display_width, display_height)) # объект экрана нашей игры
    # создаем объект спрайта основной платформы 
    sprite = Sprite_Game(150, 30, "image/4.png", display_width / 2, display_height-30, speed = 2)
    # загружает картинку спрайта в игру
    sprite.load_image()
    #
    ball = Sprite_Game(25,25, "image/arka.png", display_width / 2, display_height /2, speed = 1, speed_X = 1)
    ball.load_image()
    game = True # для работы цикла 

    path_font= os.path.join(os.path.abspath(__file__ + "/.."), "20016.ttf")

    def direction_of_travel():
        if ball.X > display_width - ball.WIDTH:
            ball.SPEED_X *= -1
        if ball.X < 0:
            ball.SPEED_X = 1
    def you_win(path_font):
        if len(list_block) < 1:
            text = pygame.font.Font(path_font, 50)
            text1 = text.render("You Win", True, (255,0,0))
            screen.blit(text1, (display_width / 2 - 50, display_height /2))
            ball.SPEED = 0
            ball.SPEED_X = 0
            ball.WIN = 1
        
    while game: # пока game будет True цикл работает
        # метод blit показывает картинку в координатах
        screen.fill((0,0,0))
       
        # рисует картинку каждого блока из списка
        for pl in list_block: 
            screen.blit(pl.END_IMAGE, (pl.X, pl.Y))
        # рисуем наш мячик
        if ball.WIN == 0:
            screen.blit(sprite.END_IMAGE, (sprite.X, sprite.Y))
            screen.blit(ball.END_IMAGE, (ball.X, ball.Y))
        # движение мячика вниз и вверх
        if move_UP_DOWN == False:
            for pl in list_block:
                if ball.RECT.colliderect(sprite.RECT):
                    move_UP_DOWN = True    
                if ball.RECT.colliderect(pl.RECT):  
                    list_block.remove(pl)
                    
                if ball.Y > display_height - ball.HEIGHT:
                    
                    text = pygame.font.Font(path_font, 50)
                    text1 = text.render("You Lose", True, (255,0,0))
                    screen.blit(text1, (display_width / 2 - 50, display_height /2))
                    ball.SPEED = 0
                    ball.SPEED_X = 0
                             
            ball.Y += ball.SPEED
            ball.X += ball.SPEED_X #
            ball.RECT.y += ball.SPEED
            ball.RECT.x += ball.SPEED_X #
            #
            direction_of_travel()   
        elif move_UP_DOWN:
            for pl in list_block:
                if ball.RECT.colliderect(pl.RECT):
                    move_UP_DOWN = False 
                if ball.RECT.colliderect(pl.RECT):
                    list_block.remove(pl)   
                if ball.Y < 0:
                    move_UP_DOWN = False    
            #  
            ball.Y -= ball.SPEED
            ball.X += ball.SPEED_X
            ball.RECT.y -= ball.SPEED
            ball.RECT.x += ball.SPEED_X
            # 
            direction_of_travel()
        # Функция победы    
        you_win(path_font)
        # 
        for event in pygame.event.get(): # 
            if event.type == pygame.QUIT: # 
                game = False # когда нажмем на крестик
            if event.type == pygame.KEYDOWN: # кнопка нажата
                if event.key == pygame.K_RIGHT:
                    move_right = True
                if event.key == pygame.K_LEFT:
                    move_left = True
            elif event.type == pygame.KEYUP: # кнопка не нажата
                if event.key == pygame.K_RIGHT:
                    move_right = False
                if event.key == pygame.K_LEFT:
                    move_left = False 
        # движение платформы в правую сторону и в левую сторону
        if  move_right:
            sprite.X += sprite.SPEED
            sprite.RECT.x += sprite.SPEED
        if move_left:
            sprite.X -= sprite.SPEED
            sprite.RECT.x -= sprite.SPEED
        
        pygame.display.flip() # обновляет экран 
        FPS.tick(240)

start_game()




