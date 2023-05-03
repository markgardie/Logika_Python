from Sprite import*
from Fireball import*
from constants import*


# таймер, який визначає проміжок часу між вистрілами
# вказують на кадри, а не секунди
# налаштування нашої гри - 60 кадрів в сек.
# отже таймер = 60 - це тривалість однієї секунди
timer = 60

# спадкується від базового класу Спрайт
# копіює хітбокс та зображення
class Boss(Sprite):

    # генерація випадкового напрямку
    def generate_direction(self):

        # напрямок може бути: -1, 0, 1
        # -1 по х це рух вліво
        # -1 по у це рух вгору
        # 1 по х це рух вправо
        # 1 по у це рух вниз
        # 0 означає, що руху по даній координатній прямій не відбувається
        direction_x = randint(-1, 1)
        direction_y = randint(-1, 1)

        # нам не треба комбінація х = 0 та у = 0
        # оскільки при таких напрямках руху не буде
        # доти поки у нас генерується цей напрямок
        # ми заново перегенеровуємо напрямки
        while direction_x == 0 and direction_y == 0:
            direction_x = randint(-1, 1)
            direction_y = randint(-1, 1)

        # повертаємо в інше місце згенеровані напрямки
        return direction_x, direction_y

    # метод вистрілу
    # приймає список фаєрболів
    # в який будуть додаватись нові фаєрболи при стрільбі
    def fire(self, fireballs):

        # робимо таймер глобальною змінною
        # аби зміни таймера всередині цієї функції
        # відобразились для всіх функцій
        global timer

        # якщо вийшов час таймер,
        # то треба стріляти
        if timer == 0:
            
            # очищаємо список фаєрболів від попередніх снарядів
            fireballs.clear()

            # генеруємо напрямки для 3 фаєрболів
            dir_1_x, dir_1_y = self.generate_direction()
            dir_2_x, dir_2_y = self.generate_direction()
            dir_3_x, dir_3_y = self.generate_direction()

            # кладемо напрямки в списки
            dir_xs = [dir_1_x, dir_2_x, dir_3_x]
            dir_ys = [dir_1_y, dir_2_y, dir_3_y]

            # проходимось циклом по всім напрямкам та комбінаціям
            for dir_x in dir_xs:
                for dir_y in dir_ys:

                    
                    # верхній-лівий напрямок
                    if dir_x == -1 and dir_y == -1:
                        fireball = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT,
                                            self.hitbox.left, self.hitbox.top,
                                            FIREBALL_PATH, FIREBALL_SPEED, 
                                            dir_x, dir_y)
                    
                    # лівий напрямок
                    if dir_x == -1 and dir_y == 0:
                        fireball = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT,
                                            self.hitbox.left, self.hitbox.centery,
                                            FIREBALL_PATH, FIREBALL_SPEED, 
                                            dir_x, dir_y)
                        
                    # лівий-нижній напрямок
                    if dir_x == -1 and dir_y == 1:
                        fireball = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT,
                                            self.hitbox.left, self.hitbox.bottom,
                                            FIREBALL_PATH, FIREBALL_SPEED, 
                                            dir_x, dir_y)
                        
                    # верхній
                    if dir_x == 0 and dir_y == -1:
                        fireball = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT,
                                            self.hitbox.centerx, self.hitbox.top,
                                            FIREBALL_PATH, FIREBALL_SPEED, 
                                            dir_x, dir_y)

                    # нижній
                    if dir_x == 0 and dir_y == 1:
                        fireball = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT,
                                            self.hitbox.centerx, self.hitbox.bottom,
                                            FIREBALL_PATH, FIREBALL_SPEED, 
                                            dir_x, dir_y)
                        
                    # правий-верхній
                    if dir_x == 1 and dir_y == -1:
                        fireball = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT,
                                            self.hitbox.right, self.hitbox.top,
                                            FIREBALL_PATH, FIREBALL_SPEED, 
                                            dir_x, dir_y)
                        
                    # правий
                    if dir_x == 1 and dir_y == 0:
                        fireball = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT,
                                            self.hitbox.right, self.hitbox.centery,
                                            FIREBALL_PATH, FIREBALL_SPEED, 
                                            dir_x, dir_y)
                    
                    # правий-нижній
                    if dir_x == 1 and dir_y == 1:
                        fireball = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT,
                                            self.hitbox.right, self.hitbox.bottom,
                                            FIREBALL_PATH, FIREBALL_SPEED, 
                                            dir_x, dir_y)
                    
                    # додаємо згенерований фаєрбол в список
                    fireballs.append(fireball)

            # таймер починається заново           
            timer = 60

        else:
            # тіки таймера
            timer -= 1
    
    # рух боса у випадкову точку
    # при торканні із гравцем
    def move(self):

        self.hitbox.x = randint(100, WINDOW_WIDTH - 100) 
        self.hitbox.y = randint(100, WINDOW_HEIGHT - 100)        
  