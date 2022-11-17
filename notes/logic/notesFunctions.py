import json
from ui.mainWindow import ui, mainWindow
from PyQt5.QtWidgets import QInputDialog
from data.dataFunctions import writeNotes, readNotes


def showNotesInfo(notes):

    noteTitle = ui.notesListWidget.selectedItems()[0].text()
    print(noteTitle)
    ui.notesTextEdit.setText(notes[noteTitle]["текст"])
    ui.tagsListWidget.clear()
    ui.tagsListWidget.addItems(notes[noteTitle]["теги"])

    
def addNote(notes):
    noteName, ok = QInputDialog.getText(mainWindow, "Додати замітку", "Назва замітки: ")
    if ok and noteName != "":
        notes[noteName] = {"текст" : "", "теги" : []}
        ui.notesListWidget.addItem(noteName)
        ui.tagsListWidget.addItems(notes[noteName]["теги"])
        writeNotes(notes)


def deleteNote(notes):
    if ui.notesListWidget.selectedItems():
        noteTitle = ui.notesListWidget.selectedItems()[0].text()
        del notes[noteTitle]

        ui.notesListWidget.clear()
        ui.tagsListWidget.clear()
        ui.notesTextEdit.clear()

        writeNotes(notes)
        readNotes()
    else:
        print("Замітка для вилучення не обрана!")

def saveNote(notes):
    if ui.notesListWidget.selectedItems():
        noteTitle = ui.notesListWidget.selectedItems()[0].text()
        notes[noteTitle]["текст"] = ui.notesTextEdit.toPlainText()

        writeNotes(notes)
    else:
        print("Замітка для збереження не вибрана!")
        