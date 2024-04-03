from ui.main_screen import Ui_MainScreen
from PyQt5.QtWidgets import QWidget, QInputDialog
from data.notes_dao import NotesDao

class NotesScreenManager():

    # конструктор
    # початкові налаштунки
    def __init__(self):


        # створення та налаштування вікна
        self.mainWidget = QWidget()
        self.mainScreen = Ui_MainScreen()
        self.mainScreen.setupUi(self.mainWidget)

        # показ вікна
        self.mainWidget.show()

        # створення репозиторія
        self.notesDao = NotesDao()

        # запуск інших функцій
        self.showNotesList()
        self.setListeners()

        # нюанси: навіщо треба репозиторій?
        # репозиторій - це клас, який зберігає дані, а також дозволяє виконувати 
        # CRUD-операції: create, read, update, delete

    # налаштування слухачів, які слідкують за кліками на кнопки
    def setListeners(self):

        # кнопки і кліки на кнопки, відповідальні за нотатки
        self.mainScreen.createNoteBtn.clicked.connect(self.createNote)
        self.mainScreen.deleteNoteBtn.clicked.connect(self.deleteNote)
        self.mainScreen.saveNoteBtn.clicked.connect(self.saveNote)

        # кнопки і кліки на кнопки, відповідальні за теги
        self.mainScreen.addTagBtn.clicked.connect(self.addTag)
        self.mainScreen.deleteTagBtn.clicked.connect(self.deleteTag)
        self.mainScreen.searchBtn.clicked.connect(self.search)

        # вибір певної нотатки в списку нотаток
        self.mainScreen.notesListWidget.itemClicked.connect(self.showNoteInfo)

    # показ списку нотаток
    def showNotesList(self):
        # отримуємо у репозиторія список нотаток
        notes = self.notesDao.getNotes()

        # додаємо всі нотатки в ListWidget
        for note in notes:
            self.mainScreen.notesListWidget.addItem(note["title"])

        # нюанси: розповісти про ListWidget
        # це віджет, який дозволяє виводити на екран список елементів,
        # а також клікати  на кожен елемент

    # показ вмісту нотаток: тексту, тегів
    def showNoteInfo(self):
        # дізнаємось назву нотатки, яка зараз обрана
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        notes = self.notesDao.getNotes()

        for note in notes:

            # отримуємо текст нотатки
            # і виводимо його в TextEdit на екран
            if  note["title"] == noteTitle:
                noteText = note["text"]
                self.mainScreen.noteTextEdit.setText(noteText)
                
                # отримуємо теги нотатки
                # додаємо їх в ListWidget тегів
                tags = note["tags"]
                self.mainScreen.tagsListWidget.clear()

                for tag in tags:
                    self.mainScreen.tagsListWidget.addItem(tag)

            # нюанси: розповісти про TextEdit
            # Це велике поле, в яке можна вписати багато тексту
            # LineEdit - це поле тільки в одну строку

    # створення нотатки
    def createNote(self):
        # запускаємо діалогове вікно, в якому запитуємо назву нотатки
        noteTitle, ok = QInputDialog.getText(self.mainWidget, "Додати нотатку", "Введіть нотатку")
        
        # створюємо нову нотатку
        # текст та теги поки пусті
        if ok and noteTitle != "":
            # додаємо нову нотатку в репозиторій
            self.notesDao.createNote(noteTitle)
            self.mainScreen.notesListWidget.addItem(noteTitle)

        # нюанси: важливо перевіряти чи правильно відпрацював QInputDialog, 
        # бо інакше може створитись пуста нотатка
        # розповісти про QInputDialog
        # це віджет, який запускає маленьке діалогове вікно із полем для вводу

    # зберігаємо новий текст нотатки
    def saveNote(self):
        # отримуємо назву та текст нотатки
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        noteText = self.mainScreen.noteTextEdit.toPlainText()
        
        if noteTitle != "":   
            # оновлюємо нотатку
            self.notesDao.updateNoteText(noteTitle, noteText)

        # нюанси: розповісти про selectedItems
        # ця функція повертає список обраниїх елементів
        # але користувач обирає тільки один елемент, тому нам треба тільки перший елемент списка
        # тому ми пишемо [0]

    # видалення нотатки
    def deleteNote(self):
        # отримуємо назву нотатки, яку треба видалити
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        
        if noteTitle != "":
            # видаляємо нотатку
            # очищаємо список нотаток і поле з текстом
            # і заново завантажуємо оновлені нотатки
            self.notesDao.deleteNote(noteTitle)
            self.mainScreen.notesListWidget.clear()
            self.mainScreen.noteTextEdit.clear()

            self.showNotesList()

        # нюанси: після видалення нотатки, сама вона з екрана не пропаде
        # нам треба це зробити вручну: очистити список нотаток і заново
        # завантажити вже новий список без видаленої нотатки

    # додати тег до нотатки
    def addTag(self):

        # отримуємо назву нотатки, яка обрана
        # отримуємо назву тегу
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        tag = self.mainScreen.searchLineEdit.text()
        
        if tag != "":
            # додаємо новий тег в репозиторій і на екран
            self.notesDao.addTag(noteTitle, tag)
            self.mainScreen.tagsListWidget.addItem(tag)

    # видалення тега
    def deleteTag(self):
        # дивимось назву нотатки і тег, який треба видалити
        noteTitle = self.mainScreen.notesListWidget.selectedItems()[0].text()
        tag = self.mainScreen.tagsListWidget.selectedItems()[0].text()
        
        if tag != "":
            # видаляємо тег
            self.notesDao.deleteTag(noteTitle, tag)

            self.mainScreen.tagsListWidget.clear()
            self.showNoteInfo()

        # нюанси: схоже на видалення нотатки - тег при видалення з екрану сам не пропаде
        # треба очистити список тегів вручну і заново завантажити оновлений список тегів

    # пошук нотаток по тегу
    def search(self):
        # із поля пошуку отримуємо назву тегу, за яким будемо шукати нотатки
        tag = self.mainScreen.searchLineEdit.text()
        if tag != "":

            # очищаємо список нотаток
            # і з репозиторія отримуємо списко вже відфільтрованих нотаток
            # показуємо на екрані
            self.mainScreen.notesListWidget.clear()

            filteredNotes = self.notesDao.search(tag)

            for note in filteredNotes:
                self.mainScreen.notesListWidget.addItem(note["title"])
        
        # аби повернути на екран список всіх нотаток треба
        # очистити поле пошуку і зробити тег пустим
        # тоді завантажеться весь список
        else:
            self.mainScreen.notesListWidget.clear()
            self.showNotesList()




        