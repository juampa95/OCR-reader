import pytesseract
from PIL import Image

image_path ='img/set1/20230420141949.bmp'

image = Image.open(image_path)

text = pytesseract.image_to_string(image)

print(text)