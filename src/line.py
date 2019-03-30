from src.tools import *
from src.constants import *

class Line:

    image = None

    line_height = 0

    width = 0

    line_gap = 0

    top_left_point = (0, 0)

    bars = []

    def __init__(self, image, top_left_point, line_height, line_gap):
        self.image = image
        self.line_height = line_height
        self.width = self.image.shape[::-1][1]
        self.line_gap = line_gap
        self.top_left_point = top_left_point

    def draw_line(self):
        draw_one_rectangle(self.image, self.top_left_point, self.width, self.line_height+self.line_gap*2, red)