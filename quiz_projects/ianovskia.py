print("                                            Вітаю тебе в вікторині!")
print("                                                    Успіхів!")
f = input("Питання 1-ше. Ти людина чи робот: ").lower()
bals = 0

def question(text, answer):
    global bals
    a = int(input(text))
    if a == answer:
        print("Молодець!")
        bals += 1
    else:
        print("Не правильно!")

def question2(text, answer):
    global bals
    b = input(text)
    if b == answer:
        print("Чудово!")
        bals += 1
    else:
        print("Не правильно!")
        
if f == "робот":
    question("Скільки буде: 7 + 7 : 7 + 7 * 7 - 7: ", 50)
    question("Скільки буде: 8 + 8 : 8 + 8 * 8 - 8: ", 65)
    question('Скільки буде: 9 + 9 : 9 + 9 * 9 - 9: ', 82)
    question("Скільки буде: 6 + 6 : 6 + 6 * 6 - 6: ", 37)
    print("                                          Вітаю ти пройшов вікторину")
    print(f"                                        Ти заробив {bals} балів")
    
if f == "людина":
    question2("Яка столиця України?", "Київ")
    question2("Яке найбільше озеро в Україні?", "Світязь")
    question2("Яке свято 31 грудня?", "Новий рік")
    question2("Перший колір веселки?", "Червоний")
    question2("Найбільший океан в світі", "Тихий" or "Тихий океан")
    question2("Найбільша пустеля в світі", "Сахара")
    print("                                          Вітаю ти пройшов вікторину")
    print(f"                                        Ти заробив {bals} балів")