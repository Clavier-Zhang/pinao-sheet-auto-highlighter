import cv2
import numpy as np
from tools import *
from helper import *
red = (0,0,255)

class Sheet:

    width = 0

    height = 0

    top_left = (0, 0)

    image = None

    lines = []

    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        self.width = self.image.shape[::-1][1]
        self.height = self.image.shape[::-1][2]
        label_all_measure(self.image, red)
        save('test.png', self.image)
        print(self.height)

    def build_lines(self):
        return 