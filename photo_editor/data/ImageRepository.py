import os
from domain.ImageEditor import ImageEditor
from PIL import Image

class ImageRepository():

    def __init__(self):
        self.extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
        self.imageEditor = ImageEditor()

    def filterFiles(self, dir):
        files = os.listdir(dir)
        filteredFiles = []

        for file in files:
            for ext in self.extensions:
                if file.endswith(ext):
                    filteredFiles.append(file)

        return filteredFiles
    
    def loadImage(self, path):
        return Image.open(path)

    def saveImage(self, image, save_path):
        image.save(save_path)

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


            

    



