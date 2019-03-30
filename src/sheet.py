import cv2
import numpy as np
from src.tools import *
from src.helper import *
from src.line import Line

red = (0,0,255)
blue = (255, 0, 0)

brace_dir = 'data/brace/'

class Sheet:

    width = 0

    height = 0

    top_left = (0, 0)

    image = None

    lines = []

    line_height = 250

    line_pos = []

    line_gap = 0

    def __init__(self, image_path, line_height):
        self.image = cv2.imread(image_path)
        self.width = self.image.shape[::-1][1]
        self.height = self.image.shape[::-1][2]
        self.line_height = line_height
        self.build_line_grids()
        self.draw_lines()
        self.draw_sheet()
        save('test.png', self.image)

    def build_line_grids(self):
        points = self.find_all_braces()
        self.line_gap = int((points[1][1]-points[0][1]-self.line_height)/2)
        for point in points:
            self.line_pos.append((0, point[1]-self.line_gap))
            self.lines.append(Line(self.image, (0, point[1]-self.line_gap), self.line_height, self.line_gap))

    def find_all_braces(self):
        result = []
        for image_path in os.listdir(brace_dir):
            if image_path.endswith(".png"):
                brace = read_template(brace_dir+image_path)
                result = result + find_all_match(self.image, brace, 0.85)
        points = remove_close_point(result, 2000)
        return points

    def draw_sheet(self):
        draw_one_rectangle(self.image, (0, 0), self.width, self.height, blue)

    def draw_lines(self):
        for line in self.lines:
            line.draw_line()
        # draw_all_rectangles(self.image, self.line_pos, self.width, self.line_height+self.line_gap*2, red)