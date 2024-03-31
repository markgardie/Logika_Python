from PIL import Image
from PIL.ImageFilter import SHARPEN
from data.editor_dao import EditorDao

class EditPhotoUseCase():

    def __init__(self):
        self.dao = EditorDao()

    def open(self, name):
        return self.dao.open(name)

    def save(self, path, image):
        self.dao.save(path, image)

    def filterFiles(self, path):
        self.dao.filterFiles(path)

    def blackAndWhite(self, original):
        return original.convert("L")
    
    def left(self, original):
        return original.transpose(Image.ROTATE_270)
    
    def right(self, original):
        return original.transpose(Image.ROTATE_90)
    
    def mirror(self, original):
        return original.transpose(Image.FLIP_LEFT_RIGHT)
    
    def sharpen(self, original):
        return original.filter(SHARPEN)
    