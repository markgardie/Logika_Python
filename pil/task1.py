from PIL import Image, ImageFilter, ImageEnhance

originalPath = r"pil\original.jpg"
savePath = r"pil\images"

with Image.open(originalPath) as original:
    gray = original.convert("L")
    gray.save(savePath + r"\gray.jpg")

    blur = original.filter(ImageFilter.BLUR)
    blur.save(savePath + r"\blur.jpg")

    mirror = original.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.save(savePath + r"\mirror.jpg")

    right = original.transpose(Image.ROTATE_90)
    right.save(savePath + r"\right.jpg")
