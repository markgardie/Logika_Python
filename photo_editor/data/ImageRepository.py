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

    def setFilename(self, name):
        self.filename = name

    def filter(self):
        files = os.listdir(self.originalDir)
        filtered_files = []

        for file in files:
            for ext in self.extensions:
                if file.endswith(ext):
                    filtered_files.append(file)

        return filtered_files

