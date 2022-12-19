import os
from PyQt5.QtWidgets import QFileDialog
from ui.photoEditorUi import*

extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp'] #розширення, які показують, що файл є растровим зображенням

#Функція, яка запускає діалогове вікно, вибору папки
def chooseWorkdir():
    workdir = QFileDialog.getExistingDirectory() #Відкривається діалогове вікно, QFileDialog, 
    #гравець обирає в цьому вікні папку з фото
    #ми отримуємо шлях до цієї папки і зберігаємо в workdir
    return workdir #повертаємо цей шлях, аби використовувати в інших функціях

def filter(files, extensions):
    filtered = [] #список відфільтрованих файлів (повинні бути фото), напочатку пустий
    for file in files: #цикл, який перебирає файли в обраній папці
        for ext in extensions: #цикл, який перевіряє розширення
            if file.endswith(ext): #якщо файл закінчується розширенням фото, то
                filtered.append(file) #додаємо цей файл в список відфільтрованих
    return filtered #повертаємо список відфільтрованих файлів, аби використати в інших функціях
    
def showFilenameList():
    workdir = chooseWorkdir() #запускаємо функцію для отримання папки з файлами
    files = os.listdir(workdir) #отримуємо файл з цієї папки
    filtered = filter(files, extensions) #фільтруємо папки

    ui.photoListWidget.clear() #очищаємо список-віджет від попередніх файлів

    for file in filtered: #проходимось по відфільтрованим файлам
        ui.photoListWidget.addItem(file) #додаємо назви цих файлів в віджет-список