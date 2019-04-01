from src.tools import *
from src.constants import *
from src.note import *
import copy

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

    line_height_A = None

    line_height_B = None

    line_height_C = None

    line_height_D = None

    note_height = None

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

        self.note_height = line_height/13.5

        self.line_height_A = top_left_point[1]+line_gap
        self.line_height_D = self.line_height_A+line_height
        self.line_height_B = self.line_height_A+int(4*self.note_height)

        self.line_height_C = self.line_height_D-int(4*self.note_height)

        
        

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
        bar_note_points = []
        for note_point in line_note_points:
            if self.contains(note_point):
                bar_note_points.append(note_point)

        top_note_points = []
        bottom_note_points = []
        middle_note_points = []

        for point in bar_note_points:
            if point[1] <= self.line_height_B:
                self.notes.append(Note(self.image, point, 'top'))
                top_note_points.append(point)
                # draw_one_rectangle(self.image, point, 10, 10, green)
            elif point[1] >= self.line_height_C:
                self.notes.append(Note(self.image, point, 'bottom'))
                bottom_note_points.append(point)
                # draw_one_rectangle(self.image, point, 10, 10, red)
            else:
                middle_note_points.append(point)

        middle_note_points.sort(key=lambda point : point[1])
        num = len(middle_note_points)
        is_top = True
        if num > 0:
            hi = middle_note_points[0]
            lo = middle_note_points[num-1]
            is_top = abs(hi[1]-self.line_height_B) < abs(lo[1]-self.line_height_C)
        print(is_top)

        if is_top:
            top_note_points = middle_note_points+top_note_points
        else:
            bottom_note_points = middle_note_points+bottom_note_points

        draw_all_rectangles(self.image, top_note_points, 10, 10, green)
        draw_all_rectangles(self.image, bottom_note_points, 10, 10, red)
    
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