import json
from ui.mainWindow import uiMainWindow

path = r"C:\Users\Марк\Desktop\Logika_Python\notes\data\greetings.json"

notes = {}


def loadNotes():
    with open(path, "r", encoding="utf-8") as file:
        notes = json.load(file)
    uiMainWindow.notesListWidget.addItems(notes)


def showNotes():

    with open(path, "r", encoding="utf-8") as file:
        notes = json.load(file)

    noteTitle = uiMainWindow.notesListWidget.selectedItems()[0].text()
    print(noteTitle)
    uiMainWindow.notesTextEdit.setText(notes[noteTitle]["текст"])
    uiMainWindow.tagsListWidget.clear()
    uiMainWindow.tagsListWidget.addItems(notes[noteTitle]["теги"])

    
