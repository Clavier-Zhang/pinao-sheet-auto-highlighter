import cv2
import numpy as np
from tools import *


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

def label_all_measure(img, color):
    measure_1 = read_template('data/measure/MEASURE_1.png')
    measure_2 = read_template('data/measure/MEASURE_2.png')
    find_all_and_label(img, measure_1, 0.85, color)
    find_all_and_label(img, measure_2, 0.9, color)