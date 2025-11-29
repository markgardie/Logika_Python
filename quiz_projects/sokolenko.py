import random

print("Перша гра — це гральні кості")
print()
print("Вітаю! Це гра в кості. Кожен гравець кидає кубик, і програма випадково визначає результат.")
print("Правила: значення може бути від 1 до 6. Гравців — двоє.")
print("Приємної гри!\n")

number_one = random.randint(1, 6)
number_two = random.randint(1, 6)

print(f"Перший гравець кинув: {number_one}")
print(f"Другий гравець кинув: {number_two}")

if number_one == number_two:
    print("Нічия! Обидва гравці отримали однаковий результат.")
elif number_one > number_two:
    print("Перший гравець виграв!")
else:
    print("Другий гравець виграв!")
