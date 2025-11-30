# бажаємо успіхів та трудолюбивості
print("Добрий день!")
print("Ласкаво просим до вікторини!")

points = 0

while True:
    difficulty = input("Виберіть складність - easy , normal або hard:").lower()
    if difficulty == "easy":
        print("Прекрасно , ви вибрали легку складність.")
        easy_question1 = input("Яка офіційна мова в нідерландах? - А = Французька; Б = Нідерладська; В = Англійська;").upper()
        if easy_question1 == "Б":
            points+=1
        #else:
        easy_question2 = input("Скільки буде 2 + 2? - А = 3; Б = 4; В = 5. ").upper()
        if easy_question2 == "Б":
            points+=1
        #else:
        easy_question3 = input("Коли Україна стала незалежною? - А = 1939р.; Б = 1991р.; В = 2012р.").upper()
        if easy_question3 == "Б":
            points+=1
        #else:
        break
    elif difficulty == "normal":
        print("Прекрасно , ви вибрали нормальну складність.")
        normal_question1 = input("Коли утворилася Київська-Русь? - А = 882р.; Б = 839р.; В = 945р.; Г = 482р.").upper()
        if normal_question1 == "А":
            points+=2
        #else:
        normal_question2 = input("Скільки буде 201 - 324 + 123? - А = 9; Б = 1; В = 3; Г = 0 ").upper()
        if normal_question2 == "Г":
            points+=2
        #else:
        normal_question3 = input("Прада чи брехня : Прислівник — це самостійна незмінна частина мови, яка означає ознаку дії, стану, ознаку іншої ознаки або предмета та відповідає на питання як? де? куди? коли? чому? навіщо? тощо. - А = Ні; Б = Так.").upper()
        if normal_question3 == "Б":
            points+=2
        #else:
        normal_question4 = input("Знайди підмет - (Танцювати - це мистецтво).").lower()
        if normal_question4 == "танцювати":
            points+=2
        #else:
        normal_question5 = input("Скільки всього океанів - А = 4 ; Б = 5 ; В = 6.").upper()
        if normal_question5 == "Б":
            points+=2
        break
    elif difficulty == "hard":
        print("Прекрасно , ви вибрали складну складність.")
        hard_question1 = input("У кого нема плавального міхура - А = лосось ; Б = короп ; В = камбала ; Г = вугор.").upper()
        if hard_question1 == "В":
            points+=3
        #else:
        hard_question2 = input("Коли випустили фільм - Зоряні війни2 - А = 2002р. ; Б = 1997р. ; В = 2005р. ; Г = 2015р.").upper()
        if hard_question2 == "А":
            points+=3
        #else:
        hard_question3 = input("Коли відкритий урок?").lower()
        if hard_question3 == "сьогодні":
            points+=3
        #else:
        hard_question4 = input("Розгадай загадку - Без рук, без ніг, а ворота відчиняє").lower()
        if hard_question4 == "вітер":
            points+=3
        #else:
        hard_question5 = input("Скільки енергії в 1 грамі жиру - А = 17,2 кДж ; Б = 38,9 кДж ; В = 53,5 кДж ; Г = 30 кДж.").upper()
        if hard_question5 == "Б":
            points+=3
        #else:
        hard_question6 = input("Розгадай загадку - З язиком, але не лається, без зубів, але кусається. Лютує та злиться, а води боїться").lower()
        if hard_question6 == "вогонь":
            points+=3
        #else:
        hard_question7 = input("Морква - це - А = Коренебульба ; Б = плід ; В = псевдокорінь ; Г = коренеплід.").upper()
        if hard_question7 == "Г":
            points+=3
        #else:
        hard_question8 = input("Яка рослина має реактивний рух - А = кактус ; Б = дикий огірок ; В = непентес ; Г = кальмар.").upper()
        if hard_question8 == "Б":
            points+=3
        #else:
        hard_question9 = input("Яка офіційна мова в Канаді? - А = Французька; Б = Німецька; В = Англійська;").upper()
        if hard_question9 == "А" or "В":
            points+=3
        #else:
        hard_question10 = input("Хто ти?").lower()
        if hard_question10 == "людина":
            points+=5
        break
        #else:
    else:
        print("Спробуйте ще раз.")
        difficulty = input("Виберіть складність - easy , normal або hard:").lower()

print(f"Ось твій результат - {points}")