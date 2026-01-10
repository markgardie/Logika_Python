
from time import *

score = 0
def question(q, right_answer):
    global score 
    user_answer = input(q + "").lower().strip()
    if user_answer == right_answer.lower():
       print("Вірно!\n")
       score += 1 
    else:
        print(f"Невірно! Правильна відповідь: {right_answer}\n")

start_time = time()      

question("- Змінна у Python?", "Ім’я для даних.")
question("- Типи даних?", "int, float, str, bool, list, tuple, dict, set.")
question("- List vs tuple?", "list змінний, tuple ні.")
question("- Dict?", "Ключ–значення.")
question("- Цикл for?", "Ітерація по елементах.")
question("- While vs for?", "while — умова; for — елементи.")
question("- Функція?", "Блок коду через def.")
question("- Mutable vs immutable?", "Mutable змінювані; immutable — ні.")
question("- Помилки?", "try, except, finally, raise.")

end_time = time()                 
elapsed_time = end_time - start_time   


if elapsed_time <= 60:
    print(f"Час виконання: {elapsed_time:.0f} секунд.")
else:
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"Час виконання: {minutes} хв {seconds} сек.")

print(f"Ваш результат: {score} з 9 балів.")

