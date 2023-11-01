import os
from domain.ImageEditor import ImageEditor
from PIL import Image

class ImageRepository():

    # конструктор
    # початкові налаштування
    def __init__(self):
        # формати файлів фото для фільтрування
        self.extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
        # редактор фото
        self.imageEditor = ImageEditor()

    # фільтруємо файли в папці
    # аби отримати тільки фото
    def filterFiles(self, dir):
        # отримуємо список всіх файлів в папці
        # створюємо пустий список відфільтрованих файлів
        files = os.listdir(dir)
        filteredFiles = []

        # фільтруємо файли перевіряючи їх формат, розширення
        for file in files:
            for ext in self.extensions:
                if file.endswith(ext):
                    filteredFiles.append(file)

        return filteredFiles
    
        # нюанси: розповісти про функцію endswith
        # вона дозволяє вказати, чи закінчується файл певним текстом
    
    # завантаження зображення по певному шляху
    def loadImage(self, path):
        return Image.open(path)

    # збереження зображення в папку Modified
    def saveImage(self, image, save_path):
        image.save(save_path)

    # ці функції самі по собі нічого не роблять
    # вони делегують (передають) свою роботу іншому класу ImageEditor
    def blackAndWhite(self, image):
        return self.imageEditor.blackAndWhite(image)
    
    def left(self, image):
        return self.imageEditor.left(image)
    
    def right(self, image):
        return self.imageEditor.right(image)
    
    def mirror(self, image):
        return self.imageEditor.mirror(image)
    
    def sharpen(self, image):
        return self.imageEditor.sharpen(image)


            

    



