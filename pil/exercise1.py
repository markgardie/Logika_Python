from PIL import Image, ImageFilter, ImageEnhance

originalPath = r"pil\original.jpg"
savePath = r"pil\images"

with Image.open(originalPath) as original:
    print("Розмір: " + original.size)
    # Формат
    # Режим
    original.show()

    gray = original.convert("L")
    gray.save(savePath + r"\gray.jpg")

    blured = original.filter(ImageFilter.BLUR)
    blured.save(savePath + r"\blured.jpg")

    up = original.transpose(Image.ROTATE_180)
    up.save(savePath + r"\up.jpg")

    mirror = original.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.save(savePath + r"\mirror.jpg")


