import pytesseract as ocr
from PIL import Image
pharse=ocr.image_to_string(Image.open('pharse.jpg'),lang='por')
print(pharse)
