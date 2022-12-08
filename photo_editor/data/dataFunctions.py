import os
from PyQt5.QtWidgets import QFileDialog
from ui.photoEditorUi import*

extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']

def chooseWorkdir():
    workdir = QFileDialog.getExistingDirectory()
    return workdir

def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result


def showFilenamesList():
    workdir = chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)

    ui.photoListWidget.clear()
    
    for filename in filenames:
        ui.photoListWidget.addItem(filename)

 

   
   