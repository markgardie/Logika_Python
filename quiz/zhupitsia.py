from time import time

score = 0

def question(h, right_answer):
    global score 
    user_answer = input(h + " ").lower()
    if user_answer == right_answer.lower():
        print("Вірно!")
        score += 1
    else:
        print(f"Невірно! Правильна відповідь: {right_answer}")

start_time = time()

question("Столиця Франції?", "Париж")
question("Скільки планет у Сонячній системі?", "8")
question("Хто написав 'Кобзар'?", "Тарас Шевченко")
question("Найбільший океан на Землі?", "Тихий")
question("У якому році людина вперше висадилась на Місяць?", "1969")
question("Хімічний символ води?", "H2O")
question("Яка мова має найбільшу кількість носіїв у світі?", "Китайська")
question("Найвища гора світу?", "Еверест")
question("Скільки хромосом у людини?", "46")
question("Яка тварина є символом Австралії?", "Кенгуру")

end_time = time()

print(f"Ваш результат: {score} із 10")
print(f"Час виконання: {end_time - start_time:.2f} секунд")
