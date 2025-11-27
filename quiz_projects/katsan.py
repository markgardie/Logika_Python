#імпорт бтеки рандом 
import random
#створення нікнеймів гравцям
user_1 = input("Введіть нікнейм гравцю 1")
user_2 = input("Введіть нікнейм гравцю 2")

#оьирання гри
while True:
    print("\nОберіть:")
    print("1 - Гральні кості")
    print("3 - Закінчити")
    choose = int(input())
#розділення на ігри
    if choose == 1:
        pl1 = 0
        pl2 = 0
        def randomizer1():
            res1 = random.randint(1, 6)
            print(f"{user_1} випало {res1}")
            return res1
        def randomizer2():
            res2 = random.randint(1, 6)
            print(f"{user_2} випало {res2}")
            return res2
        for i in range (3):
            print(f"\nРаунд {i+1}:")
            us1 = randomizer1()
            us2 = randomizer2()
    
            if us1 > us2:
                print(f"{user_1} переміг {i+1}й раунд")
                pl1 += 1
            elif us2 > us1:
                print(f"{user_2} переміг {i+1}й раунд")
                pl2 += 1
            else:
                print("Нічия")
        if pl1 > pl2:
            print(f"\n{user_1} переміг матч: ({pl1} бали)")
        elif pl2 > pl1:
            print(f"\n{user_2} переміг матч: ({pl2} бали)")
        else:
            print("Нічия!")
    elif choose == 3:
        print("Закінчення...")
        break
    else: 
        print("Такої команди не існує, спробуйте ще раз.")

    