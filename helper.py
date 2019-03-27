import cv2
import numpy as np
from tools import *
import os

measure_dir = 'data/measure/'
# def find_all_braces(image):
#     for file_path in 
def find_all_bass(img):
    bass_1 = read_template('data/bass/BASS_1.png')
    raw_points = find_all_match(img, bass_1, 0.8)
    return remove_close_point(raw_points, 200)

def label_all_bass(img, color):
    bass_1 = read_template('data/bass/BASS_1.png')
    find_all_and_label(img, bass_1, 0.6, color)

def label_all_sharp(img, color):
    sharp_1 = read_template('data/sharp/SHARP_1.png')
    find_all_and_label(img, sharp_1, 0.6, color)

def label_all_treble(img, color):
    treble_1 = read_template('data/treble/TREBLE_1.png')
    find_all_and_label(img, treble_1, 0.5, color)

def label_all_natural(img, color):
    natural_1 = read_template('data/natural/NATURAL_1.png')
    find_all_and_label(img, natural_1, 0.7, color)

def label_all_measure(image, color):
    result = []
    for image_path in os.listdir(measure_dir):
        if image_path.endswith(".png"):
            measure = read_template(measure_dir+image_path)
            result = result + find_all_match(image, measure, 0.85)

    points = remove_close_point(result, 2000)

    draw_all_rectangles(image, points, 50, 50, color)
