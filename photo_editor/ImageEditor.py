from PIL import Image
from PIL.ImageFilter import SHARPEN

class ImageEditor():

    def blackAndWhite(self, image):
        return image.convert("L")
    
    def left(self, image):
        return image.transpose(Image.ROTATE_270)
    
    def right(self, image):
        return image.transpose(Image.ROTATE_90)
    
    def mirror(self, image):
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    
    def sharpen(self, image):
        return image.filter(SHARPEN)