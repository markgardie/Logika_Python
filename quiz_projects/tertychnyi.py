def question(q, right_answer, wrong1, wrong2, wrong3):
    print(f"{q} а - {right_answer}, б - {wrong1}, в - {wrong2}, г - {wrong3}")
    user_answer = input().lower()
    if user_answer == right_answer.lower():
        print("Вірно!")
    else:
        print("Не вірно")
    
question("Столиця України? " , "Київ", "Харків", "Вінниця", "Житомир")
question("Найшвидша тварина у світі? ", "Гепард")
question("Скільки планет в сонячній системі? " , "8", "4", "67", "1")
question("Найшвидша тварина у світі? ", "Гепард")
question("Столиця України? " , "Київ", )
question("Найшвидша тварина у світі? ", "Гепард")
question("Столиця України? " , "Київ", )
question("Найшвидша тварина у світі? ", "Гепард")
question("Столиця України? " , "Київ", )
question("Найшвидша тварина у світі? ", "Гепард")