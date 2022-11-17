
from ui.mainWindow import ui
from data.dataFunctions import writeNotes, readNotes

def addTag(notes):
    if ui.notesListWidget.selectedItems():
        notesTitle = ui.notesListWidget.selectedItems()[0].text()
        tag = ui.searchLineEdit.text()
        if not tag in notes[notesTitle]["теги"]:
            notes[notesTitle]["теги"].append(tag)
            ui.tagsListWidget.addItem(tag)
            ui.searchLineEdit.clear()
        
        writeNotes(notes)
    else:
        print("Замітка для додавання тега не обрана!")


def deleteTag(notes):
    if ui.tagsListWidget.selectedItems():
        noteTitle = ui.notesListWidget.selectedItems()[0].text()
        tag = ui.tagsListWidget.selectedItems()[0].text()
        notes[noteTitle]["теги"].remove(tag)
        ui.tagsListWidget.clear()
        ui.tagsListWidget.addItems(notes[noteTitle]["теги"])
        writeNotes(notes)
    else:
        print("Тег для вилучення не обраний!")
