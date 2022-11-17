
from ui.mainWindow import uiMainWindow
from data.dataFunctions import writeNotes, readNotes

def addTag(notes):
    if uiMainWindow.notesListWidget.selectedItems():
        notesTitle = uiMainWindow.notesListWidget.selectedItems()[0].text()
        tag = uiMainWindow.searchLineEdit.text()
        if not tag in notes[notesTitle]["теги"]:
            notes[notesTitle]["теги"].append(tag)
            uiMainWindow.tagsListWidget.addItem(tag)
            uiMainWindow.searchLineEdit.clear()
        
        writeNotes(notes)
    else:
        print("Замітка для додавання тега не обрана!")


def deleteTag(notes):
    if uiMainWindow.tagsListWidget.selectedItems():
        noteTitle = uiMainWindow.notesListWidget.selectedItems()[0].text()
        tag = uiMainWindow.tagsListWidget.selectedItems()[0].text()
        notes[noteTitle]["теги"].remove(tag)
        uiMainWindow.tagsListWidget.clear()
        uiMainWindow.tagsListWidget.addItems(notes[noteTitle]["теги"])
        writeNotes(notes)
    else:
        print("Тег для вилучення не обраний!")
