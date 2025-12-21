print("Вітаємо вас в грі “Вгадай число”!🎉")
print("Бажаю успіхів!")
from random import randint
import time as t
a = randint(1 , 150)
count = 0
start_time = t.time()
while True:
    number = int(input("Введіть число:"))
    count += 1
    if number > a:
        print("Ваше число більше!")
    elif number < a:
        print("Ваше число менше!")
    else:
        print("✅Відповідь вірна!")
        break
end_time = t.time()
ansver_time = end_time - start_time
ansver_time = round(ansver_time)
print(f"Кількість спроб: {count}")
print(f"Ваш час: {ansver_time}")
if count >= 5:
    print("Молодець, продовжуй і в тебе все вийде!🙂")
elif count <= 2:
    print("Молодець, це було швидко!🔥")
elif count == 1:
    print("Тобі пощастило!✨")
else:
    print("Продовжуй і все вийде!🤗")
if ansver_time < 2:
    print("Молодець, це було дуже швидко!🔥")
elif ansver_time > 20:
    print("Я знаю, ти можеш швидче!🤗")
elif ansver_time < 5 and ansver_time > 2:
    print("Круто! Це було швидко!😃")   
elif ansver_time <10:
    print("Не погано. Але постарайся швидче!😉")
else:
    print("Це було дуже повільно. Постарайся швидче!🙁")