import pytesseract
from PIL import Image, ImageOps, ImageFilter
import time
import tempfile
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extact_text(img, cfg):
    if type(img) == str:
        image = Image.open(img)
        text = pytesseract.image_to_string(image, config=cfg)
        return text
    else:
        text = pytesseract.image_to_string(img, config=cfg)
        return text


def img_binary(image_path, t):
    image = Image.open(image_path)
    image = image.convert('L').point(lambda p: p > t and 255)
    return image


def img_transf(image_path, threshold, noise):
    image = Image.open(image_path)
    binary_image = image.convert('L').point(lambda p: p > threshold and 255)
    denoise_image = binary_image.filter(ImageFilter.MedianFilter(size=noise))
    enhanced_image = ImageOps.equalize(denoise_image)
    background_color = (255, 255, 255)
    transparent_image = enhanced_image.convert('RGBA')
    data = transparent_image.getdata()
    new_data = []
    for item in data:
        if item[:3] == background_color:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    transparent_image.putdata(new_data)
    text_image = transparent_image.convert('L')
    artifcat_remove_image = text_image.filter(ImageFilter.SMOOTH_MORE)
    return artifcat_remove_image


custom_config = f'--oem 3 --psm 4'
image_dir = 'img/set1'

files = os.listdir(image_dir)
len(files)

results = []

for file in files:
    file_path = os.path.join(image_dir,file)
    if file.endswith('.bmp'):
        text = extact_text(img_binary(file_path, 140)
                           , custom_config)
        text = text.split('\n')
        text = list(filter(bool,text))
        if '07793397052082' in text[0] and 'AUROLUO' in text[1] and '17/05/2026' in text[2]:
            results.append('OK')
            print('OK   ',text)
        else:
            results.append('ERROR')
            print('ERROR',text)


print(results)
