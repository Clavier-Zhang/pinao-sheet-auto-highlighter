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

    bars = None

    front_sharp_points = None
    
    front_flat_points = []

    front_natural_points = []

    # solve this later
    sharp_flat_range = 200

    def __init__(self, image, top_left_point, line_height, line_gap, all_bar_line_points):
        self.image = image
        self.line_height = line_height
        self.width = image.shape[::-1][1]
        self.line_gap = line_gap
        self.top_left_point = top_left_point
        self.bars = []

        self.front_sharp_points = []

        self.construct_bars(all_bar_line_points)

        note_height = line_height/13.5

    def construct_bars(self, all_bar_line_points):
        
        bar_line_points = self.get_points_inside(all_bar_line_points)

        bar_line_points.sort(key=lambda bar_line_point : bar_line_point[0])

        for i in range(0, len(bar_line_points)-1):
            bar_line_point_start = bar_line_points[i]
            bar_line_point_end = bar_line_points[i+1]
            width = bar_line_point_end[0]-bar_line_point_start[0]
            top_left_point = (bar_line_point_start[0], self.top_left_point[1])
            bar = Bar(self.image, top_left_point, width, self.line_height, self.line_gap)
            self.bars.append(bar)

    def analyze_notes(self, all_note_points):

        line_note_points = self.get_points_inside(all_note_points)

        for bar in self.bars:
            bar.analyze_notes(line_note_points)




    def analyze_sharp_and_flat_points(self, all_sharp_points, all_flat_points, all_natural_points):

        line_sharp_points = []
        line_flat_points = []
        line_natural_points = []

        line_sharp_num = 0
        line_flat_num = 0

        for sharp_point in all_sharp_points:
            if (self.contains(sharp_point)):
                line_sharp_points.append(sharp_point)
                if sharp_point[0] < self.bars[0].top_left_point[0]+self.sharp_flat_range:
                    line_sharp_num += 1
                    self.front_sharp_points.append(sharp_point)
                    line_sharp_points.remove(sharp_point)

        for flat_point in all_flat_points:
            if (self.contains(flat_point)):
                line_flat_points.append(flat_point)
                if flat_point[0] < self.bars[0].top_left_point[0]+self.sharp_flat_range:
                    line_flat_num += 1
                    self.front_flat_points.append(flat_point)
                    line_flat_points.remove(flat_point)

        for natural_point in all_natural_points:
            if (self.contains(natural_point)):
                line_natural_points.append(natural_point)
                if natural_point[0] < self.bars[0].top_left_point[0]+self.sharp_flat_range:
                    line_natural_points.remove(natural_point)
                    self.front_natural_points.append(natural_point)

        for bar in self.bars:
            bar.analyze_sharp_and_flat_points(line_sharp_points, line_flat_points, line_sharp_num/2, line_flat_num/2, line_natural_points)

    
    def get_points_inside(self, points):
        temp = []
        for point in points:
            if self.contains(point):
                temp.append(point)
        return temp

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

    def draw_notes(self):
        for bar in self.bars:
            bar.draw_notes()

    def draw_sharp_flat_natural(self):
        draw_all_rectangles(self.image, self.front_sharp_points, 25, 50, red)
        draw_all_rectangles(self.image, self.front_natural_points, 25, 50, green)
        draw_all_rectangles(self.image, self.front_flat_points, 25, 50, amethyst)
        for bar in self.bars:
            bar.draw_sharp_flat_natural()