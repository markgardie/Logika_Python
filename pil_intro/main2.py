from PIL import Image
from PIL import ImageFilter

originalPath = r"C:\Users\Марк\Desktop\Logika_Python\pil_intro\original2.jpg" 
class ImageEditor():
    def __init__(self, path):
        self.path = path
        self.original = None
        self.changed = list()
 
    def open(self):
        try:
            self.original = Image.open(self.path)
        except:
            print('Файл не знайдено!')
        self.original.show()
 
    def do_left(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)
 
    #бонус. Обрізка
    def do_cropped(self):
        box = (250, 100, 600, 400) #вліво, вгору, вправо, вниз
        cropped = self.original.crop(box)
        self.changed.append(cropped)
 
MyImage = ImageEditor(originalPath)
MyImage.open()
 
MyImage.do_left()
MyImage.do_cropped()
 
for im in MyImage.changed:
    im.show()
