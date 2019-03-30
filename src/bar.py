from src.tools import *
from src.constants import *

class Bar:

    image = None

    top_left_point = None

    width = None

    line_height = None

    line_gap = None

    def __init__(self, image, top_left_point, width, line_height, line_gap):
        self.image = image
        self.top_left_point = top_left_point
        self.width = width
        self.line_height = line_height
        self.line_gap = line_gap

    def draw_bar(self):
        height = self.line_height + self.line_gap*2
        draw_one_rectangle(self.image, self.top_left_point, self.width, height, blue)