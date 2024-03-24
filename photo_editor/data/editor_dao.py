import os
from PIL import Image

class EditorDao():

    def __init__(self):
        self.extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']

    def filterFiles(self, path):
        allFiles = os.listdir(path)
        filteredFiles = []

        for file in allFiles:
            for ext in self.extensions:
                if file.endswith(ext):
                    filteredFiles.append(file)

        return filteredFiles
    
    def open(self, path):
        return Image.open(path)
    
    def save(self, path, image):
        image.save(path)

    



    