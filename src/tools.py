import cv2
import numpy as np
import os


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

def draw_text(image, top_left_point, text, color):
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10,500)
    fontScale = 1.2
    lineType = 2
    cv2.putText(image, str(text), top_left_point, font, fontScale, color, lineType)



def convert_grey(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def find_all_match(img, template, confidnece):
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= confidnece)
    points = list(zip(*loc[::-1]))
    return points

def find_all_dir_templates(image, dir, confidence, close_range):
    result = []
    image = convert_grey(image)
    for image_path in os.listdir(dir):
        if image_path.endswith(".png") or image_path.endswith(".jpg"):
            template = read_template(dir+image_path)
            result = result + find_all_match(image, template, confidence)
    points = remove_close_point(result, close_range)
    return points





def save(filename, img):
    cv2.imwrite(filename, img)

def read(image_path):
    return cv2.imread(image_path)

def read_template(templatepath):
    return cv2.imread(templatepath, 0)




def remove_close_point(points, range):
    selecteds = []
    for point in points:
        keep = True
        for selected in selecteds:
            diff = (point[0]-selected[0])**2 + (point[1]-selected[1])**2
            if diff < range:
                keep = False
        if keep:
            selecteds.append(point)
    return selecteds
