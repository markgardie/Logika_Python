import os
from domain.ImageEditor import ImageEditor
from PIL import Image


class ImageRepository():

    def __init__(self):
        self.extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
        self.originalDir = None
        self.filename = None
        self.saveDir = r"\Modified"
        self.imageEditor = ImageEditor()


    def setOriginalDir(self, dir):
        self.originalDir = dir

    def loadImage(self, name):
        self.filename = name
        path = os.path.join(self.originalDir, self.filename)
        self.image = Image.open(path)

    def saveImage(self):
        path = os.path.join(self.originalDir, self.saveDir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        self.image.save(path)

    def filter(self):
        files = os.listdir(self.originalDir)
        filtered_files = []

        for file in files:
            for ext in self.extensions:
                if file.endswith(ext):
                    filtered_files.append(file)

        return filtered_files
    
    def blackAndWhite(self):
        self.image = self.imageEditor.blackAndWhite(self.image)

