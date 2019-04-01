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
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10,500)
    fontScale              = 1
    lineType               = 2
    cv2.putText(image, str(text), top_left_point, font, fontScale, color, lineType)




def find_all_match(img, template, confidnece):
    img = convert_grey(img)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= confidnece)
    points = list(zip(*loc[::-1]))
    return points

def find_all_dir_templates(image, dir, confidence, close_range):
    result = []
    for image_path in os.listdir(dir):
        if image_path.endswith(".png"):
            template = read_template(dir+image_path)
            result = result + find_all_match(image, template, confidence)
    points = remove_close_point(result, close_range)
    return points

def find_all_dir_templates_test(image, dir, confidence, close_range):
    result = []
    for image_path in os.listdir(dir):
        if image_path.endswith(".png"):
            template = read_template(dir+image_path)
            result = result + find_all_match(image, template, confidence)
    return result


def convert_grey(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def save(filename, img):
    cv2.imwrite(filename, img)

def read(image_path):
    return cv2.imread(image_path)

def read_template(templatepath):
    return cv2.imread(templatepath, 0)

def in_the_same_vertical_line(p1, p2, range):
    return abs(p1[0]-p2[0]) < range

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

def remove_vertical_close_point(points, range):
    results = []
    for point in points:
        keep = True
        for result in results:
            if abs(point[1]-result[1]) < range:
                keep = False
        if keep:
            results.append(point)
    return results

def mouse_call_back(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print((x, y))
        
def get_point(imagePath):
    img = cv2.imread(imagePath)
    cv2.imshow('image',img)
    cv2.setMouseCallback('image', mouse_call_back)
    result = cv2.waitKey(0)
    cv2.destroyAllWindows()

def crop(image, top_left, width, height):
    return image[top_left[1]:top_left[1]+height, top_left[0]:top_left[0]+width]