score = 0   
def question2(q, right_answer):
    user_answer = input(q + ": ").Кlower()
    if user_answer == right_answer.lower():
        print("Вірно!")
        return 1     
    else:
        print("Не вірно!")
        return 0      
score += question2("Столиця України", "Київ")
score += question2("Столиця Польщі", "Варшава")
score += question2("Столиця Німеччини", "Берлін")
score += question2("Столиця Франції", "Париж")
score += question2("Столиця Молдови", "Кишинів")
score += question2("Столиця Румунії", "Бухарест")
score += question2("Столиця Італії", "Рим")
score += question2("Столиця Іспанії", "Мадрид")
score += question2("Столиця Португалії", "Лісабон")
score += question2("Столиця Туреччини", "Анкара")
score += question2("Столиця Естонії", "Таллінн")
score += question2("Столиця Латвії", "Рига")
score += question2("Столиця Литви", "Вільнюс")
score += question2("Столиця Великої Британії", "Лондон")
score += question2("Столиця Китаю", "Пекін")
score += question2("Столиця Індії", "Нью-Делі")
score += question2("Столиця Америки", "Вашингтон")
score += question2("Столиця Японії", "Токіо")
score += question2("Столиця Єгипту", "Каїр")
score += question2("Столиця Бразилії", "Бразиліа")
score += question2("Столиця Мексики", "Мехіко")
print("\nВаш результат:", score, "балів із 20")