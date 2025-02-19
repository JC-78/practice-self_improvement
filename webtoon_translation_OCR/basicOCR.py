
from PIL import Image
import pytesseract
import numpy as np
filename = 'image_01.png'
#filename ='/Users/joonghochoi/Desktop/OCR/translation-example.jpg'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)
print(text)
