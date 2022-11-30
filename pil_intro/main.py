from PIL import Image, ImageFilter, ImageEnhance

originalPath = r"C:\Users\Марк\Desktop\Logika_Python\pil_intro\original.jpg"
savePath = r"C:\Users\Марк\Desktop\Logika_Python\pil_intro"

with Image.open(originalPath) as original:

    print('Розмір:', original.size)
    print('Формат:', original.format)
    print('Тип:', original.mode) 
    original.show()
 
    gray = original.convert('L')    
    gray.save(savePath + r"\gray.jpg")
    print('Розмір:', gray.size)
    print('Формат:', gray.format)
    print('Тип:', gray.mode) 
    gray.show()
 
    blured = original.filter(ImageFilter.BLUR)
    blured.save(savePath + r'\blured.jpg')
    blured.show()
 
    up = original.transpose(Image.ROTATE_180)
    up.save(savePath + r'\up.jpg')
    up.show()
 

    mirrow = original.transpose(Image.FLIP_LEFT_RIGHT)
    mirrow.save(savePath + r'\mirrow.jpg')
    mirrow.show()
 
    contrast = ImageEnhance.Contrast(original)
    contrast = contrast.enhance(1.5)
    contrast.save(savePath + r'\contr.jpg')
    contrast.show()
