from ui.mainWindow import ui
from data.dataFunctions import*

def showNotes(notes):

    noteTitle = ui.notesListWidget.selectedItems()[0].text()
    print(noteTitle)
    ui.notesTextEdit.setText(notes[noteTitle]["текст"])
    ui.tagsListWidget.clear()
    ui.tagsListWidget.addItems(notes[noteTitle]["теги"])