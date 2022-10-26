#напиши тут свою програму
import os


path = r"C:\Users\Марк\Desktop\Logika_Python\files\quotes.txt"

with open(path, "r", encoding = "UTF-8") as file:
    for line in file:
        print(line)
 
author = input("Хто написав ці рядки? ")
with open(path, "a",  encoding = "UTF-8") as file:
    file.write(f"({author})\n")
 
while True:
    answer = input("Бажаєте додати ще одну цитату? (так / ні)")
    answer = answer.lower()
    if answer == "так":
        quote = input("Введіть цитату: ")
        author = input("Введіть автора: ")
        file = open(path, "a",  encoding = "UTF-8")
        file.write(f"{quote}\n({author})\n")
        file.close()
    else:
        break
 
with open(path, "r", encoding = "UTF-8") as file:
    for line in file:
        print(line)




