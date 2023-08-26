path = r"D:\Mark\Desktop\Logika_Python\files\quotes.txt"

with open(path, "r", encoding="utf-8") as file:
    for line in file:
        print(line)

author = input("Хто автор?")
with open(path, "a", encoding="utf-8") as file:
    file.write(f"({author})")

