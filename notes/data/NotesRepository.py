import json

class NotesRepository():

    # конструктор
    # виконуються початкові налаштування репозиторія
    def __init__(self):
        # збереження даних в списку (тимчасове)
        self.notes = []
        # шлях до файлу для постійного збереження
        self.path = r"D:\Mark\Desktop\Logika_Python\notes\data\notes.json"

        # нюанси: r-строка для ігнорування слешів (\) і керуючих символів
        # список зберігає дані тимчасово, але зручний в роботі
        # файл зберігає дані постійно, але незручний в роботі

    # збереження нових даних у файлі
    def saveFile(self):
        # відкриття файлу
        # завантаження списку у файл
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(self.notes, file)

        # нюанси: обережно з режимами відкриття файла: тільки читання чи переписування

    # створення нотатки
    def createNote(self, newNote):
        # нова нотатка додається в список
        self.notes.append(newNote)
        self.saveFile()

        # нюанси: нотатка являється словником
        # notes - це по суті список словників


    # читання нотаток із файла
    def readNotes(self):
        # відкриття файла і збереження даних в список
        with open(self.path, "r", encoding="utf-8") as file:
            self.notes = json.load(file)

    # оновлення тексту нотатки
    def updateNote(self, noteTitle, noteText):
        # перебирання списку нотаток
        # пошук нотатки по заголовоку (назві)
        for note in self.notes:
            if note["title"] == noteTitle:
                note["text"] = noteText

        # збереження змін у файл
        self.saveFile()

    # видалення нотатки
    def deleteNote(self, noteTitle):
        # перебирання списку нотаток
        # пошук нотатки по заголовоку (назві)
        for note in self.notes:
            if note["title"] == noteTitle:
                self.notes.remove(note)

        # збереження змін у файл
        self.saveFile()

    # додавання тегу
    def addTag(self, noteTitle, tag):
        # шукаємо нотатку, в яку треба цей тег додати
        for note in self.notes:
            if note["title"] == noteTitle:
                note["tags"].append(tag)

        # зберігаємо зміни
        self.saveFile()

    # отримання списку тегів певної нотатки
    def readTags(self, noteTitle):
        # шукаємо нотатку
        # у неї отримуємо список тегів
        for note in self.notes:
            if note["title"] == noteTitle:
                return note["tags"]
    
    # видалення тегів
    def deleteTag(self, noteTitle, tag):
        # шукаємо нотатку, в якій треба видалити тег
        # видаляємо тег
        for note in self.notes:
            if note["title"] == noteTitle:
                note["tags"].remove(tag)

        self.saveFile()

    # пошук нотаток по тегам
    def searchByTag(self, searchTag):
        # список нотаток, які мають шуканий тег
        filteredNotes = []

        # перебираємо список нотаток
        # і забираємо (фільтруємо) тільки ті, що мають шуканий тег
        for note in self.notes:
            for tag in note["tags"]:
                if tag == searchTag:
                    filteredNotes.append(note)

        # повертаємо відфільтровані нотатки
        return filteredNotes