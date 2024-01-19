from PIL import Image
import numpy as np
import pytesseract 
from googletrans import Translator

translator = Translator()

filename = 'b.jpg'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)

if text == "":
    text = 'None'

print(text)