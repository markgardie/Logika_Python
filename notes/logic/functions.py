import json
from ui.mainWindow import uiMainWindow, mainWindow
from PyQt5.QtWidgets import QInputDialog
from data.data import writeNotes


def showNotesInfo(notes):

    noteTitle = uiMainWindow.notesListWidget.selectedItems()[0].text()
    print(noteTitle)
    uiMainWindow.notesTextEdit.setText(notes[noteTitle]["текст"])
    uiMainWindow.tagsListWidget.clear()
    uiMainWindow.tagsListWidget.addItems(notes[noteTitle]["теги"])

    
def addNote(notes):
    noteName, ok = QInputDialog.getText(mainWindow, "Додати замітку", "Назва замітки: ")
    if ok and noteName != "":
        notes[noteName] = {"текст" : "", "теги" : []}
        uiMainWindow.notesListWidget.addItem(noteName)
        uiMainWindow.tagsListWidget.addItems(notes[noteName]["теги"])
        writeNotes(notes)
        