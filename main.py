import cv2
import numpy as np
from tools import *
from helper import *
from sheet import Sheet

red = (0,0,255)
green = (0,255,0)
pink = (255,0,255)
blue = (255,0,0)
light_blue = (255,255,0)

line_height = 17

def match_all(imagePath):
    # img = cv2.imread(imagePath)

    # points = find_all_bass(img)
    
    # print(points)

    # top_left = points[0]

    # label_all_bass(img, green)

    # label_all_sharp(img, red)

    # label_all_treble(img, pink)

    # label_all_natural(img, blue)

    # label_all_measure(img, light_blue)

    # save('res1.png', img[top_left[1]-17:top_left[1],top_left[0]:3000])

    return


# match_all('sample.png')

# get_point('sample.png')


sheet = Sheet('sample.png')