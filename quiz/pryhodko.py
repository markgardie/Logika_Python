from random import randint

def dice_game():
    print("Гра в кісті")
    print("               ")
    
    player1 = input("Гравець 1: ")
    player2 = input("Гравець 2: ")
    
    score1 = 0
    score2 = 0
    
    for round in range(3):
        print(f"Раунд {round+1}")
        
        print(player1 + ", кидає кість")
        dice = randint(1, 6)
        guess = int(input("Вгадай число (1-6): "))
        
        if guess == dice:
            score1 = score1 + 1
            print("Вірно!")
        else:
            print("Невірно! Було", dice)
        
        print(player2 + ", кидає кість")
        dice = randint(1, 6)
        guess = int(input("Вгадай число (1-6): "))
        
        if guess == dice:
            score2 = score2 + 1
            print("Вірно!")
        else:
            print("Невірно! Було", dice)
    
    print("Результати:")
    print(player1 + ":", score1, "балів")
    print(player2 + ":", score2, "балів")
    
    if score1 > score2:
        print("Переміг:", player1)
    elif score2 > score1:
        print("Переміг:", player2)
    else:
        print("Нічия!")

while True:
    print("1 - Грати")
    print("2 - Вийти")
    c = input("Вибір: ")
    
    if c == "1":
        dice_game()
        again = input("Грати ще? (так/ні): ")
        if again == "ні":
            break
    elif c == "2":
        break