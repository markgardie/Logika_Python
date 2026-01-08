# бажаємо успіхів та трудолюбивості
from time import time

score = 0
def question(h, right_answer):
    global score 
    user_answer = (h + " ").lower()
    if user_answer == right_answer.lower():
        print("Вірно!")
        score += 1
    else:
        print(f"Невірно! Правильна відповідь: {right_answer}")
start_time = time()
question("")
question("")
question("")
question("")
question("")
question("")
question("")
question("")
question("")
question("")
end_time = time()
print(f"Ваш результат: {score} із 10")
print(f"{end_time - start_time}")