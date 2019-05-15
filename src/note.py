import math
from src.tools import *
from src.constants import *

class Note:

    image = None

    top_left_point = None

    is_top = None

    half_note_height = None

    origin_line = None

    def __init__(self, image, top_left_point, is_top, half_note_height, origin_line):
        self.image = image
        self.top_left_point = top_left_point
        self.is_top = is_top
        self.half_note_height = half_note_height
        self.origin_line = origin_line

        self.analyze_pitch()

    def analyze_pitch(self):
        count = 0
        target_height = self.top_left_point[1]
        start_height = self.origin_line
        if self.is_top:

            if target_height >= self.origin_line:
                while start_height < target_height:
                    start_height += self.half_note_height
                    count += 1
            else:
                count += 1
                while start_height > target_height:
                    start_height -= self.half_note_height
                    count -= 1
                while count < 0:
                    count += 7
            count %= 7
            

        else:

            if target_height >= self.origin_line:
                while start_height < target_height:
                    start_height += self.half_note_height
                    count += 1
            else:
                count += 1
                while start_height+3 > target_height:
                    start_height -= self.half_note_height
                    count -= 1
                while count < 0:
                    count += 7
            count %= 7

        self.pitch = top_note_dict[count]

    def draw_note(self):
        color = red
        if self.is_top:
            color = green

        draw_one_rectangle(self.image, self.top_left_point, 33, 28, color)

        draw_text(self.image, (self.top_left_point[0]+45, self.top_left_point[1]+15), self.pitch, blue)

      