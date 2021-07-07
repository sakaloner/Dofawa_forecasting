from PIL import Image
import pytesseract, time, re, os, cv2, csv
from icecream import ic
import numpy as np
import cv2

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

print(normalize("¡Hólá, múndó!"))
print(normalize("¡HÓLÁ, MÚNDÓ!"))

exit()





pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Test shit
im = Image.open('objetos/2.png')
#print(im.size)

im_price = im.crop((480,0,525,43))
#im_price.show()


from PIL import Image



# abrir la imagen con cv2
img = cv2.imread("objetos/2.png")
# cambiarla a blanco y negro
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# volverlo un acrhivo de PIL
t = Image.fromarray(np.uint8(grayImage*255))
#c crop
t = t.crop((480,0,525,43))
t.show()
# leerlo
p = pytesseract.image_to_string(t)
print(p)
exit()

p = pytesseract.image_to_string(t)
print(p)
exit()
cv2.imshow('perro', t)
cv2.waitKey(0)

p = pytesseract.image_to_data(grayImage)
print(p)


price = clean(pytesseract.image_to_string(im_price))
price = ''.join(price.split())
print(price)
print(int(price))

exit()