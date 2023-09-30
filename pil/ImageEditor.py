from PIL import Image
from PIL import ImageFilter

class ImageEditor():

    def __init__(self, path):
        self.path = path
        self.original = None

    def openImage(self):
        try:
            self.original = Image.open(self.path)
        except:
            print("Файл не знайдено")

        