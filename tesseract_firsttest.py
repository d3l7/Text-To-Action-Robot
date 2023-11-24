from PIL import Image
import numpy as np
import pytesseract 
from googletrans import Translator

translator = Translator()

filename = 'a.png'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)

text = translator.translate(text, dest='en')

if text == "":
    text = 'None'

print(text)