import json
from ui.mainWindow import ui

path = r"C:\Users\Марк\Desktop\Logika_Python\notes\data\notes.json"

def readJson():
    with open(path, "r", encoding="utf-8") as file:
        notes = json.load(file)

    ui.notesListWidget.addItems(notes)

    return notes

def writeJson(notes):
    with open(path, "w", encoding="utf-8"):
        json.dump(notes, sort_keys=True, ensure_ascii=True)