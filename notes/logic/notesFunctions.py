import json
from ui.mainWindow import uiMainWindow, mainWindow
from PyQt5.QtWidgets import QInputDialog
from data.dataFunctions import writeNotes, readNotes


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


def deleteNote(notes):
    if uiMainWindow.notesListWidget.selectedItems():
        noteTitle = uiMainWindow.notesListWidget.selectedItems()[0].text()
        del notes[noteTitle]

        uiMainWindow.notesListWidget.clear()
        uiMainWindow.tagsListWidget.clear()
        uiMainWindow.notesTextEdit.clear()

        writeNotes(notes)
        readNotes()
    else:
        print("Замітка для вилучення не обрана!")

def saveNote(notes):
    if uiMainWindow.notesListWidget.selectedItems():
        noteTitle = uiMainWindow.notesListWidget.selectedItems()[0].text()
        notes[noteTitle]["текст"] = uiMainWindow.notesTextEdit.toPlainText()

        writeNotes(notes)
    else:
        print("Замітка для збереження не вибрана!")
        