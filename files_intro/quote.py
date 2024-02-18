
path = r"D:\Mark\Desktop\Logika_Python\files_intro\quote.txt"

with open(path, "a", encoding="utf-8") as file:
    author = "\nТарас Шевченко"
    file.write(author)

with open(path, "r", encoding="utf-8") as file:
    poem = file.read()