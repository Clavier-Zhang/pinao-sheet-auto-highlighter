from src.tools import *
from src.constants import *

class Bar:

    image = None

    top_left_point = None

    width = None

    line_height = None

    line_gap = None

    bar_sharp_points = None

    bar_flat_points = None

    bar_natural_points = None

    notes = None

    def __init__(self, image, top_left_point, width, line_height, line_gap):
        self.image = image
        self.top_left_point = top_left_point
        self.width = width
        self.line_height = line_height
        self.line_gap = line_gap
        self.bar_sharp_points = []
        self.bar_flat_points = []
        self.bar_natural_points = []
        self.notes = []
        

    def analyze_sharp_and_flat_points(self, line_sharp_points, line_flat_points, line_sharp_num, line_flat_num, line_natural_points):

        for sharp_point in line_sharp_points:
            if self.contains(sharp_point):
                self.bar_sharp_points.append(sharp_point)

        for flat_point in line_flat_points:
            if self.contains(flat_point):
                self.bar_flat_points.append(flat_point)

        for natural_point in line_natural_points:
            if self.contains(natural_point):
                self.bar_natural_points.append(natural_point)

    def analyze_notes(self, line_note_points):
        for note_point in line_note_points:
            if self.contains(note_point):
                self.notes.append(note_point)
        draw_one_rectangle(self.image, self.top_left_point, 100, 100, green)
        print(self.top_left_point)
        print(len(self.notes))
        # print(bar_note_points)

    def contains(self, point):
        x = point[0]
        y = point[1]
        x_in_range = self.top_left_point[0] < x and x < self.top_left_point[0]+self.width
        y_in_range = self.top_left_point[1] < y and y < self.top_left_point[1]+self.line_height+self.line_gap*2
        return x_in_range and y_in_range

    def draw_bar(self):
        height = self.line_height + self.line_gap*2
        draw_one_rectangle(self.image, self.top_left_point, self.width, height, blue)

    def draw_sharp_flat_natural(self):
        draw_all_rectangles(self.image, self.bar_sharp_points, 25, 50, amber)
        draw_all_rectangles(self.image, self.bar_flat_points, 25, 50, amethyst)
        draw_all_rectangles(self.image, self.bar_natural_points, 25, 50, pink)