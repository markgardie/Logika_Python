

path = "C:\Users\Марк\Desktop\Logika_Python\files\shevchenko.txt"

with open(path, "r",  encoding="utf-8") as file:
    for line in file:
        print(line)