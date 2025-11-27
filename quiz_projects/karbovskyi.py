def question(q, right_answer):
    user_answer = input(q).lower()
    while True:
        if user_answer == right_answer.lower():
            print("Вірно!")
            return
        else:
            print("Не Вірно!")
            user_answer = input("q").lower()
    

    

question("Столиця України", "Київ")
question("Столиця Польщі", "Варшава")
question("Столиця Німеччини", "Берлін")
question("Столиця Франції", "Париж")
question("Столиця Молдови", "Кишинів")
question("Столиця Румунії", "Бухарест")
question("Столиця Італії", "Рим")
question("Столиця Іспанії", "Мадрид")
question("Столиця Португалії", "Лісабон")
question("Столиця Турції", "Стамбул")
question("Столиця Естонії", "Талінн")
question("Столиця Латвії", "Рига")
question("Столиця Литви", "Вільнюс")
question("Столиця Великої Британії", "Лондон")
question("Столиця Китаю", "Пекін")
question("Столиця Індії", "Нью-Делі")
question("Столиця Америки", "Вашингтон")
question("Столиця Японії", "Токіо")
question("Столиця Єгипту", "Каїр")