from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance


original_path = "D:\Mark\Desktop\Logika_Python\pil-intro\dog.jpg"
gray_path = "D:\Mark\Desktop\Logika_Python\pil-intro\dog-gray.jpg"

with Image.open(original_path) as original:
    print("Розмір:", original.size)
    print("Формат:", original.format)
    print("Кольорова схема:", original.mode)

    original.show()

    gray = original.convert("L")
    left = original.transpose(Image.ROTATE_270)
    blur = original.filter(ImageFilter.BLUR)

    gray.save(gray_path)