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
            points+=1
        #else:
        normal_question2 = input("Скільки буде 201 - 324 + 123? - А = 9; Б = 1; В = 3; Г = 0 ").upper()
        if normal_question2 == "Г":
            points+=1
        #else:
        normal_question3 = input("Прада чи брехня : Прислівник — це самостійна незмінна частина мови, яка означає ознаку дії, стану, ознаку іншої ознаки або предмета та відповідає на питання як? де? куди? коли? чому? навіщо? тощо. - А = Ні; Б = Так.").upper()
        if normal_question3 == "Б":
            points+=1
        #else:
        normal_question4 = input("Знайди підмет - (Танцювати - це мистецтво).").lower()
        if normal_question4 == "танцювати":
            points+=1
        #else:
        break
    elif difficulty == "hard":
        print("Прекрасно , ви вибрали складну складність.")
    else:
        print("Спробуйте ще раз.")
        difficulty = input("Виберіть складність - easy , normal або hard:").lower()

print(f"Ось твій результат - {points}")
        


