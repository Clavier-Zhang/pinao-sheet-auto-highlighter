from src.tools import *
from src.constants import *
from src.bar import *
import os


class Line:

    image = None

    line_height = 0

    width = 0

    line_gap = 0

    top_left_point = (0, 0)

    bars = []

    def __init__(self, image, top_left_point, line_height, line_gap, all_bar_line_points):
        self.image = image
        self.line_height = line_height
        self.width = image.shape[::-1][1]
        self.line_gap = line_gap
        self.top_left_point = top_left_point
        self.bar_line_points = []

        self.build_bars(all_bar_line_points)
        

    def build_bars(self, all_bar_line_points):
        bar_line_points = []
        for bar_line_point in all_bar_line_points:
            if (self.contains(bar_line_point)):
                bar_line_points.append(bar_line_point)

        for i in range(0, len(bar_line_points)-1):
            bar_line_point_start = bar_line_points[i]
            bar_line_point_end = bar_line_points[i+1]
            width = bar_line_point_end[0]-bar_line_point_start[0]
            top_left_point = (bar_line_point_start[0], self.top_left_point[1])
            bar = Bar(self.image, top_left_point, width, self.line_height, self.line_gap)
            self.bars.append(bar)

        print(bar_line_points)

    def label_all_bar_lines(self):
        result = []
        for image_path in os.listdir(bar_line_dir):
            if image_path.endswith(".png"):
                bar_line = read_template(bar_line_dir+image_path)
                result = result + find_all_match(self.image, bar_line, 0.85)

        points = remove_close_point(result, 2000)

        draw_all_rectangles(self.image, points, 50, 50, red)

    def contains(self, point):
        x = point[0]
        y = point[1]
        x_in_range = self.top_left_point[0] < x and x < self.top_left_point[0]+self.width
        y_in_range = self.top_left_point[1] < y and y < self.top_left_point[1]+self.line_height+self.line_gap*2
        return x_in_range and y_in_range

    def draw_line(self):
        draw_one_rectangle(self.image, self.top_left_point, self.width, self.line_height+self.line_gap*2, red)

    def draw_bars(self):
        for bar in self.bars:
            bar.draw_bar()