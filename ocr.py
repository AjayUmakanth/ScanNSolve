import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import cv2
import pytesseract
from PIL import Image

def filter(img):
    blur = cv2.bilateralFilter(img,9,75,75)
    blur = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    blur = cv2.dilate(blur, kernel, iterations=1)
    blur = cv2.erode(blur, kernel, iterations=1)
    ##blur = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    return blur
def ocr(path):
    img = cv2.imread(path)
    text=filter(img)
    pytesseract.pytesseract.tesseract_cmd= 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
    out = pytesseract.image_to_string(text)
    out=out.replace('\"','^')
    out=out.replace('—','-')
    out=out.replace(" ","")
    return out
