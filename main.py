import cv2
import numpy as np
from tools import *
from sheet import *

red = (0,0,255)
green = (0,255,0)
pink = (255,0,255)
blue = (255,0,0)
light_blue = (255,255,0)

line_height = 17

def match_all(imagePath):
    img = cv2.imread(imagePath)

    label_all_bass(img, green)

    label_all_sharp(img, red)

    label_all_treble(img, pink)

    label_all_natural(img, blue)

    label_all_measure(img, light_blue)

    save('res1.png', img)


match_all('sample2.png')
