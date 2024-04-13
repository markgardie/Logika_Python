from PIL import Image
from PIL.ImageFilter import SHARPEN

class EditPhotoUseCase:

    def __init__(self):
        self.dao = EditorDao()

    def open(self, path):
        return self.dao.open(path)

    def save(self, path, image):
        self.dao.save(path, image)

    def filterFiles(self, path):
        self.dao.filterFiles(path)

    def gray(self, original):
        return original.convert("L")


