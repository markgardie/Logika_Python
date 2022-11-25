
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


def searchByTag(notes):
    tag = ui.searchLineEdit.text()
    searchButtonText = ui.tagSearchButton.text()

    if searchButtonText == "Шукати по тегу" and tag:
        notesFiltered = {}

        for note in notes:
            if tag in notes[note]["теги"]:
                notesFiltered[note] = notes[note]

        ui.tagSearchButton.setText("Скинути пошук")
        ui.notesListWidget.clear()
        ui.tagsListWidget.clear()

        ui.notesListWidget.addItems(notesFiltered)
    
    elif searchButtonText == "Скинути пошук":
        ui.searchLineEdit.clear()
        ui.notesListWidget.clear()
        ui.tagsListWidget.clear()

        ui.notesListWidget.addItems(notes)

        ui.tagSearchButton.setText("Шукати по тегу")
    
