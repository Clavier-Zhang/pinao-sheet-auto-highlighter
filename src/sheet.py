import cv2
import numpy as np
from src.tools import *
from src.helper import *
from src.line import Line
from src.constants import *

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

        self.build_lines()

        self.draw_lines()
        self.draw_sheet()

        save('test.png', self.image)

    def build_lines(self):
        brace_points = self.find_all_braces()
        bar_line_points = self.find_all_bar_lines()
        self.line_gap = int((brace_points[1][1]-brace_points[0][1]-self.line_height)/2)
        for brace_point in brace_points:
            line = Line(self.image, (0, brace_point[1]-self.line_gap), self.line_height, self.line_gap, bar_line_points)
            self.lines.append(line)

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

    def find_all_bar_lines(self):
        result = []
        for image_path in os.listdir(bar_line_dir):
            if image_path.endswith(".png"):
                bar_line = read_template(bar_line_dir+image_path)
                result = result + find_all_match(self.image, bar_line, 0.85)

        points = remove_close_point(result, 5000)

        draw_all_rectangles(self.image, points, 50, 50, red)
        return points