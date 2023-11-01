from ui.MainScreen import MainScreen
from data.ImageRepository import ImageRepository
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class ScreenManager():

    # конструктор
    # початкові налаштунки
    def __init__(self):

        # створення та налаштування вікна
        self.mainWidget = QWidget()
        self.mainScreen = MainScreen()
        self.mainScreen.setupUi(self.mainWidget)

        # створення репозиторія
        self.repository = ImageRepository()

        # показ вікна
        self.mainWidget.show()

        # запуск інших функцій
        self.clickListeners()

        # нюанси: навіщо треба репозиторій?
        # репозиторій - це клас, який зберігає дані, а також дозволяє виконувати 
        # CRUD-операції: create, read, update, delete

    # налаштування слухачів, які слідкують за кліками на кнопки
    def clickListeners(self):

        # кнопки і кліки на кнопки, відповідальні за редагування фото
        self.mainScreen.folderButton.clicked.connect(self.chooseDir)
        self.mainScreen.leftButton.clicked.connect(self.left)
        self.mainScreen.rightButton.clicked.connect(self.right)
        self.mainScreen.mirrorButton.clicked.connect(self.mirror)
        self.mainScreen.sharpnessButton.clicked.connect(self.sharpen)
        self.mainScreen.grayButton.clicked.connect(self.blackAndWhite)

        # вибір певного фото в списку фотографій
        self.mainScreen.photoListWidget.itemClicked.connect(self.getClickedImageName)

    # вибір папки з фото
    def chooseDir(self):
        # діалогове вікно, в якому обераємо папку
        self.dir = QFileDialog.getExistingDirectory()
        # показуємо список фото
        self.showPhotoList()

        # нюанси: діалогове вікно - це невелике тимчасове вікно, ціль якого надати певне
        # повідомлення і попросити користувача виконати певну дію

    # показ списку фото в певній папці
    def showPhotoList(self):
        # очищаємо ListWidget від попереднього списку
        # отримуємо відфільтровані файли
        self.mainScreen.photoListWidget.clear()
        photoList = self.repository.filterFiles(self.dir)
        
        # показуємо відфільтровані файли
        for photo in photoList:
            self.mainScreen.photoListWidget.addItem(photo)

    # коли клікаємо на назву зображення
    # треба отримати цю назву
    def getClickedImageName(self):
        
        # якщо якесь зображення взагалі обране
        if self.mainScreen.photoListWidget.currentRow() >= 0:
            
            # отримуємо назву і формуємо шлях 
            self.photoName = self.mainScreen.photoListWidget.currentItem().text()
            self.path = os.path.join(self.dir, self.photoName)

            self.showImage()

            # нюанси: розповісти про join
            # це функція безпечного з'єднання двох шляхів, яка 
            # самостійно ставить слеши (\) і форматує шлях
        
    # показати обране зображення
    def showImage(self):

        # спочатку ховаємо лейбл, поки Pixmap
        # підвантажить фото
        self.mainScreen.photoLabel.hide()

        # створення та налаштування QPixmap
        # підлаштування розмірів QPixmap до розмірів лейбла
        pixmapImage = QPixmap(self.path)
        width = self.mainScreen.photoLabel.width()
        height = self.mainScreen.photoLabel.height()
        pixmapImage = pixmapImage.scaled(width, height, Qt.KeepAspectRatio)

        self.mainScreen.photoLabel.setPixmap(pixmapImage)

        # показуємо лейбл після налаштування QPixmap
        self.mainScreen.photoLabel.show()

        # нюанси: розповісти про QPixmap
        # це по суті сітка, яка накладається на лейбл, а на цю сітку
        # можна вже накласти фото
        # таким чином не треба використовувати додаткові віджети

    # Загальне пояснення для всіх наступних функцій: вони дуже схожі
    # відрізняються лише деякі назви
    def left(self):

        # завантажуємо зображення
        image = self.repository.loadImage(self.path)

        # модифікуємо зображення
        modified_image = self.repository.left(image)

        # створюємо шлях, куди зберігати
        self.path = os.path.join(self.dir, "Modified", self.photoName)

        # зберігаємо нове зображення
        self.repository.saveImage(modified_image, self.path)

        self.showImage()

    # нюанси: нагадати основі функції бібліотеки PIL
    # convert: конвертувати кольорову схемі (в даному випадку в чорно-білу)
    # transpose: повороти і відзеркалення
    # filter: накладання фільтрів та ефектів

    def right(self):
        image = self.repository.loadImage(self.path)
        modified_image = self.repository.right(image)
        self.path = os.path.join(self.dir, "Modified", self.photoName)
        self.repository.saveImage(modified_image, self.path)

        self.showImage()

    def mirror(self):
        image = self.repository.loadImage(self.path)
        modified_image = self.repository.mirror(image)
        self.path = os.path.join(self.dir, "Modified", self.photoName)
        self.repository.saveImage(modified_image, self.path)

        self.showImage()


    def sharpen(self):
        image = self.repository.loadImage(self.path)
        modified_image = self.repository.sharpen(image)
        self.path = os.path.join(self.dir, "Modified", self.photoName)
        self.repository.saveImage(modified_image, self.path)

        self.showImage()

    def blackAndWhite(self):
        image = self.repository.loadImage(self.path)
        modified_image = self.repository.blackAndWhite(image)
        self.path = os.path.join(self.dir, "Modified", self.photoName)
        self.repository.saveImage(modified_image, self.path)

        self.showImage()



            
    
