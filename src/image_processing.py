from PIL import Image, ImageEnhance, ImageFilter

def enhance_image(image):#
    gray_image = image.convert('L')
    enhancer = ImageEnhance.Contrast(gray_image)
    enhanced_image = enhancer.enhance(2)
    sharpened_image = enhanced_image.filter(ImageFilter.SHARPEN)
    return sharpened_image