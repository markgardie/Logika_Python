
import json
from ui.mainWindow import ui
from PyQt5.QtWidgets import QInputDialog


path = r"C:\Users\Марк\Desktop\Logika_Python\notes\data\notes.json"


def readNotes():
    with open(path, "r", encoding="utf-8") as file:
        notes = json.load(file)
    ui.notesListWidget.addItems(notes)

    return notes

def writeNotes(newData):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(newData, file, sort_keys=True, ensure_ascii=False)
