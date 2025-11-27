# бажаємо успіхів та трудолюбивостіimport random
import time
import random

score = 0

def question(text, answer):
    """Функція задає питання та повертає True/False."""
    print(text)
    user = input("Твоя відповідь: ").strip()
    return user.lower() == answer.lower()  # робимо перевірку без урахування регістру

print("Легкий тест з різними питаннями")
print("Початок через 3 секунди...")
time.sleep(3)

# 1
if question("1) Скільки буде 2 + 2?\n1) 3\n2) 4\n3) 5", "2"):
    score += 1

# 2
if question("2) Яка пора року найхолодніша?\n1) Літо\n2) Осінь\n3) Зима", "3"):
    score += 1

# 3
if question("3) Скільки днів у тижні?\n1) 5\n2) 6\n3) 7", "3"):
    score += 1

# 4 — random
rand = random.randint(1, 5)
if question(f"4) Введи рандомне число ", str(rand)):
    score += 1

# 5 — кольори
if question("5) Якого кольору небо вдень?\n1) Синє\n2) Зелёное\n3) Червоне", "1"):
    score += 1

# 6 — тварини
if question("6) Яка тварина каже 'гав-гав'?\n1) Кіт\n2) Собака\n3) Корова", "2"):
    score += 1

# 7 — фрукти
if question("7) Який фрукт жовтий?\n1) Банан\n2) Вишня\n3) Слива", "1"):
    score += 1

print("\nПеревіряю результат...")
time.sleep(1)

print(f"Твій результат: {score}/7")

if score == 7:
    print("🔥 Молодець! Ідеально!")
elif score >= 5:
    print("✨ Дуже добре")
else:
    print("💛 Не переживай, ще потренуємось!")
