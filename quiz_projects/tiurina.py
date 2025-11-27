import time

main_questions = [
   {"question": "Хто виграв найбільше Золотих м’ячів в історії?", "answer": "Leo Messi"},
    {"question": "Хто виграв найбільше титулів Ліги чемпіонів серед клубів?", "answer": "Real Madrid"},
    {"question": "Хто став першим гравцем, що виграв Золотий м’яч тричі поспіль?", "answer": "Michel"},
    {"question": "Хто був найкращим бомбардиром Ліги чемпіонів 2014 року?", "answer": "C.Ronaldo"},
    {"question": "Який клуб виграв Лігу чемпіонів у сезоні 2022/23?", "answer": "Manchester City"},
    {"question": "Хто став першим англійським гравцем, який виграв Золотий м’яч?", "answer": "Stanley Matthews"},
    {"question": "Хто забив головою вирішальний гол у фіналі Ліги чемпіонів 2014?", "answer": "Sergio Ramos"},
    {"question": "Хто виграв Золотий м’яч у 2018 році після Чемпіонату світу в Росії?", "answer": "Luka Modric"},
    {"question": "Який клуб програв Barcelona у фіналі Ліги чемпіонів 2011 року?", "answer": "Manchester United"},
    {"question": "Хто став наймолодшим володарем Золотого м’яча?", "answer": "Ronaldo.N"},
    {"question": "Хто виграв Лігу чемпіонів з трьома різними клубами?", "answer": "Clarence Seedorf"},
    {"question": "Хто виграв Золотий м’яч у 2022 році?", "answer": "Karim Benzema"},
    {"question": "Хто став першим воротарем, який виграв Золотий м’яч?", "answer": "Lev Yashin"},
    {"question": "Який гравець забив хет-трик у фіналі Ліги чемпіонів 1969 року?", "answer": "Prati"},
    {"question": "Хто був найкращим бомбардиром Ліги чемпіонів сезону 2020/21?", "answer": "Haaland"}
]

extra_questions = [
    {"question": "Яка країна виграла перший Чемпіонат світу з футболу?", "answer": "Уругвай"},
    {"question": "Хто забив найбільше голів за один турнір ЧС?", "answer": "Just Fontaine"},
    {"question": "Який гравець виграв ЧС тричі?", "answer": "Pele"},
    {"question": "Яка країна приймала ЧС у 2002 році разом з Японією?", "answer": "Південна Корея"},
    {"question": "Хто був найкращим бомбардиром ЧС 2010?", "answer": "Muller"}
]

def ask_questions(question_list):
    correct = 0
    for q in question_list:
        answer = input(q["question"] + " ")
        if answer.strip().lower() == q["answer"].lower():
            print("✅ Правильно!")
            correct += 1
        else:
            print(f"❌ Неправильно. Правильна відповідь: {q['answer']}")
    return correct

def run_quiz():
    print("⚽️ Починаємо футбольне опитування!")
    start_time = time.time()

    main_score = ask_questions(main_questions)
    extra_score = 0

    print(f"\n🔢 Основний результат: {main_score}/{len(main_questions)}")

    choice = input("\nХочете пройти ще 5 складних питань про Чемпіонат світу? (так/ні): ")
    if choice.strip().lower() == "так":
        print("\n🔥 Режим підвищеної складності: Чемпіонат світу")
        extra_score = ask_questions(extra_questions)
        print(f"\n🎯 Додатковий результат: {extra_score}/{len(extra_questions)}")
    else:
        print("\n✅ Опитування завершено. Дякуємо!")

    end_time = time.time()
    total_score = main_score + extra_score
    total_questions = len(main_questions) + (len(extra_questions) if extra_score > 0 else 0)
    total_time = round(end_time - start_time, 2)

    print(f"\n🏁 Основний результат: {total_score}/{total_questions}")
    print(f"⏱️ Загальний час проходження: {total_time} секунд")

# Цикл повтору
while True:
    run_quiz()
    repeat = input("\nБажаєте пройти опитування ще раз? (так/ні): ")
    if repeat.strip().lower() != "так":
        print("👋 До зустрічі!")
        break
