import cv2
from PIL import Image
from pytesseract import pytesseract
from process_image import process_image_for_ocr

img = process_image_for_ocr('test2.png', IMAGE_SIZE=1800)
img2 = process_image_for_ocr('ap-physics-c-mech-frq-2017-02.png',IMAGE_SIZE=1800)
# img = cv2.imread(test)

print(pytesseract.image_to_string(img2))
# OR explicit beforehand converting
# print(pytesseract.image_to_string(Image.fromarray(img)))
