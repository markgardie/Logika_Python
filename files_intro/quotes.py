
path = r"D:\Mark\Desktop\Logika_Python\files_intro\quotes.txt"

with open(path, "r", encoding="utf-8") as file:
    poem = file.read()
    print(poem)

with open(path, "a", encoding="utf-8") as file:
    file.write("Тарас Шевченко")