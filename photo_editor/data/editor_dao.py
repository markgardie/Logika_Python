import os
from PIL import Image


class EditorDao():

    def __init__(self):
        self.extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']

    def open(self, name):
        return os.path.join(self.dirPath, name)
    

C:/User/Desktop/Images/dog.png
    