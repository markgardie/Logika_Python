import os
from PyQt5.QtWidgets import QFileDialog

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
 

   
   