import os
from PIL import Image




class EditorDao():

    def __init__(self):
        self.extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']

    def open(self, name):
        return os.path.join(self.dirPath, name)

    def filterFiles(self, path):
        self.dirPath = path

        allFiles = os.listdir(path)
        filteredFiles = []

        for file in allFiles:
            for ext in self.extensions:
                if file.endswith(ext):
                    filteredFiles.append(file)
        
        return filteredFiles
    
    def save(self, path, image):
        image.save(path)