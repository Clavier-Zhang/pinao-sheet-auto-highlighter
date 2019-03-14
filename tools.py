import cv2
import numpy as np

def draw_one_rectangle(img, top_left_point, width, height, color):
    bottom_right_point = (top_left_point[0] + width, top_left_point[1] + height)
    cv2.rectangle(img, top_left_point, bottom_right_point, color, 2)

def draw_all_rectangles(img, top_left_points, width, height, color):
    for top_left_point in top_left_points:
        bottom_right_point = (top_left_point[0] + width, top_left_point[1] + height)
        cv2.rectangle(img, top_left_point, bottom_right_point, color, 2)
    
def draw_one_horizontal_line(img, left_end, width, height, color):
    right_end = (left_end[0] + width, left_end[1])
    cv2.line(img, left_end, right_end, color, height)





def find_all_and_label(img, template, confidence, color):
    points = find_all_match(img, template, confidence)
    width, height = template.shape[::-1]
    draw_all_rectangles(img, points, width, height, color)

def find_all_match(img, template, confidnece):
    img = convert_grey(img)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= confidnece)
    points = list(zip(*loc[::-1]))
    return points

def convert_grey(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def save(filename, img):
    cv2.imwrite(filename, img)

def read_template(templatepath):
    return cv2.imread(templatepath, 0)


def remove_close_point(points, range):
    selecteds = []
    for point in points:
        for selected in selecteds:
            diff = (point[0]-selected[0])**2 + (point[1]-selected[1])**2
            if diff < range:
                selecteds.append(point)
    return selected