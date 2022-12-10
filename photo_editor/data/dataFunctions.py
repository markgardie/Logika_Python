import os
from PyQt5.QtWidgets import QFileDialog
from ui.photoEditorUi import*

extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']

def chooseWorkdir():
    workdir = QFileDialog.getExistingDirectory()
    return workdir

def filter(files, extensions):
    filtered = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                filtered.append(file)
    return filtered
    
def showFilenameList():
    workdir = chooseWorkdir()
    files = os.listdir(workdir)
    filtered = filter(files, extensions)

    ui.photoListWidget.clear()

    for file in filtered:
        ui.photoListWidget.addItem(file)