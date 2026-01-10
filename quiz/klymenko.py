from time import *

score = 0

def question(q, right_answer):
    global score
    user_answer = input(q + " ").lower().strip()
    if user_answer == right_answer.lower():
        print("Вірно!\n")
        score += 1
    else:
        print(f"Невірно! Правильна відповідь: {right_answer}\n")

question("У якому році помер Чингісхан?", "1227")
question("Як він помер?", "Він впав з коня")
question("Хто є Хубілай-хан для Чингісхана?", "Хубілай — його онук")
question("Скільки у Чингісхана було дітей?", "Близько 2000, але відомі чотири сини")
question("Що зробив Хубілай?", "Створив династію Юань")
question("Чим цікавився Хубілай-хан у дитинстві?", "Китайською культурою")
question("Хто була головною жінкою Чингісхана?", "Оєлун (Хоелун)")
question("Як звали синів Чингісхана?", "Угедей, Толуй, Джучі")

print(score)