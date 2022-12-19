import os
from PIL import Image, ImageFilter
from ui.photoEditorUi import *
from PyQt5.QtGui import QPixmap

class ImageProcessor():

    def __init__(self):
        self.image = None #зображення, поки ми його не відкрили, тому властивість пуска
        self.dir = None #шлях до папки із зображеннями, не відкрили, пустка
        self.filename = None #назва файлу-фото
        self.saveDir = "Modified" #всі модифіковані файли будуть зберігатись в підпапку Modified

    def setDir(self, dir):
        self.dir = dir #отримуємо за допомогою дата-функцій шлях до папки, надаємо цей шлях нашому обробнику фото (ImageProcessor)

    def loadImage(self, filename):
        self.filename = filename #зберігаємо назву файлу в нашому обробнику 
        imagePath = os.path.join(self.dir, filename) #з'єднуємо шлях до папки і назву файлу, отримуємо повний шлях до файлу
        self.image = Image.load(imagePath) #завантажуємо зображення по шлях вище

    def showImage(self):
        ui.photoLabel.clear() #очищаємо наш лейбл від попереднього фото
        pixmapImage = QPixmap() #створюємо сітку (QPixmap), за допомогою якої накладемо фото поверх лейбла
        w = ui.photoLabel.width() #отримуємо ширину лейбла
        h = ui.photoLabel.height() #отримуємо висоту лейбла, це треба для того, аби фото було розмір із лейбл
        pixmapImage = pixmapImage.scaled(w, h) #змінюємо розмір сітки, аби вона була розміром із лейбл
        ui.photoLabel.setPixmap(pixmapImage) #накладаємо сітку на лейбл
        ui.photoLabel.show() #показуємо лейбл

    
            
