from PIL import Image
from PIL.ImageFilter import SHARPEN

class EditPhotoUseCase:

    def __init__(self):
        self.dao = EditorDao()

    def open(self, path):
        self.dao.open(path)

    def save(self, path):
        self.dao.save(path)

    def gray(self, original):
        return original.convert("L")

