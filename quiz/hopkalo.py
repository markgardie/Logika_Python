from time import*

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


question("- Що таке змінна у Python?", "Іменоване посилання на значення, яке зберігається в пам’яті.")
question("- Які основні типи даних існують у Python?", "int, float, str, bool, list, tuple, dict, set.")
question("- Чим відрізняється список (list) від кортежу (tuple)?", "list змінний (mutable), tuple незмінний (immutable).")
question("- Для чого використовується словник (dict)?", "Для зберігання пар «ключ–значення».")
question("- Що таке цикл for і коли його застосовують?", "Використовується для проходження по елементах послідовності (ітерація).")
question("- Чим відрізняється цикл while від for?", "while виконується, поки умова істинна; for проходить по елементах.")
question("- Що таке функція у Python і як її оголосити?", "Блок коду з ім’ям, який виконує дію; оголошується через def.")
question("- Що означає поняття 'mutable' та 'immutable' у Python?", "Mutable — можна змінювати після створення (list, dict, set). Immutable — не можна змінювати (str, tuple, int).")
question("- Як у Python обробляються помилки (exceptions)?", "За допомогою конструкцій try, except, finally, raise.")
question("- Що таке модуль і як його імпортувати?", "Модуль — файл з кодом Python; імпортується через import.")
end_time = time()
print(f"Ваш результат: {score} із 10.")

