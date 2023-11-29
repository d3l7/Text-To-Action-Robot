from PIL import Image
from pytesseract import Output
import numpy as np
import pytesseract 
import cv2

filename = '3_python-ocr.jpg'
img = np.array(Image.open(filename))
data = cv2.imread(filename)

norm_img = np.zeros((img.shape[0], img.shape[1]))

img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
img = cv2.GaussianBlur(img, (1,1), 0)

text = pytesseract.image_to_string(img)
cv2.imwrite('aaa.jpg', img)
data2 = cv2.imread('aaa.jpg')
results1 = pytesseract.image_to_data(data, output_type=Output.DICT)
results2 = pytesseract.image_to_data(data2, output_type=Output.DICT)
print(results1)
print(results2)

