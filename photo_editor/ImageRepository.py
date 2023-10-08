import os
from domain.ImageEditor import ImageEditor

class ImageRepository():

    def __init__(self):
        self.extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
        self.originalDir = None
        self.filename = None
        self.saveDir = r"\Modified"

    def setOriginalDir(self, dir):
        self.originalDir = dir

    def setFilename(self, filename):
        self.filename = filename

    def filterFiles(self):
        files = os.listdir(self.originalDir)
        filteredFiles = []

        for file in files:
            for ext in self.extensions:
                if file.endswith(ext):
                    filteredFiles.append(file)

        return filteredFiles
    
    def loadImage(self, filename):
        self.filename = filename
        self.image = Image.open(self.originalDir + self.filename)

    def saveImage(self):
        path = self.originalDir + self.saveDir
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        self.image.save(path)

            

    



