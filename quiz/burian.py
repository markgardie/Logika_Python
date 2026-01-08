import time

questions = {
    "Скільки буде 5 + 7? ": "12",
    "Столиця України? ": "Київ",
    "Скільки днів у тижні? ": "7",
    "Який колір має прапор України зверху? ": "Синій",
    "Якою мовою ми зараз програмуємо? ": "пайтон",
    "Скільки букв в українському алфавіті? ": "33",
    "Який океан найбільший? ": "Тихий",
    "Скільки секунд у одній хвилині? ": "60",
    "Скільки місяців у році? ": "12",
    "Який рік має 366 днів? ": "Високосний"
}

def quiz():
    score = 0
    start_time = time.time()

    for question, correct_answer in questions.items():
        answer = input(question)

        while answer.strip() != correct_answer:
            print("Неправильно. Спробуйте ще раз.")
            answer = input(question)

        print("Правильно!\n")
        score += 1

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print("Опитування завершено!")
    print(f"Правильних відповідей: {score} з {len(questions)}")
    print(f"Час проходження: {total_time} секунд")

while True:
    quiz()
    repeat = input("\nХочете пройти опитування ще раз? (так/ні): ").lower()
    if repeat != "так":
        print("Дякуємо за участь!")
        break