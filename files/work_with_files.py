


path = r"C:\Users\Марк\Desktop\Logika_Python\files\shevchenko.txt"

with open(path, "r",  encoding="utf-8") as file:
    for line in file:
        print(line)

author = input("Хто написав вірш?")
with open(path, "a",  encoding="utf-8") as file:
    file.write(f"({author})")

while True:
    answer = input("Чи додати цитату?")
    answer.lower()
    if answer == "ні":
        break
    if answer == "так":

        quote =  input("Введіть цитату:")
        author = input("Введіть автора:")

        with open(path, "a", encoding="utf-8") as file:
            file.write(f"{quote} \n ({author}) \n")

with open(path, "r",  encoding="utf-8") as file:
    for line in file:
        print(line)