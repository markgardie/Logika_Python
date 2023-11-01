from PIL import Image
from PIL.ImageFilter import SHARPEN

class ImageEditor():

    # перетворення зображення в чорном біле
    def blackAndWhite(self, image):
        # для цього треба конвертувати кольорову схему
        # важливі кольорові схеми: L (чорно-біла), RGBA (кольорова)
        # RGBA = red, green, blue, alpha
        # alpha - це прозорість
        return image.convert("L")
    
    # загальне пояснення для функцій поворотів
    # використовується функція transpose
    # для поворотів треба ROTATE
    # для відзеркалень - FLIP
    # повороти відбуваються проти годинниковою стрілки
    def left(self, image):
        return image.transpose(Image.ROTATE_90)
    
    def right(self, image):
        return image.transpose(Image.ROTATE_270)
    
    def mirror(self, image):
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    
    # фільтри накладаються функцією filter
    # деякі важливі фільтри: різкість, розмитість (блюр), згладжування 
    def sharpen(self, image):
        return image.filter(SHARPEN)