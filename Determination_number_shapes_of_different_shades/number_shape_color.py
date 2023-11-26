import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import regionprops
from skimage.morphology import label
from skimage.color import rgb2hsv

def count_figures_by_color(image_path):
    image = plt.imread(image_path)
    hsv = rgb2hsv(image)
    hue = hsv[:, :, 0]

    labeled = label(image.mean(2) > 0)
    regions = regionprops(labeled)

    circle_colors = []
    rectangle_colors = []
    num_rectangles = 0
    num_circles = 0

    for region in regions:
        hue_values = hue[tuple(zip(*region.coords))]
        unique_hues = np.unique(hue_values)
        for h in unique_hues:
            aspect_ratio = region.minor_axis_length / region.major_axis_length
            shape = 'Rectangle' if aspect_ratio > 0.99 else 'Circle'
            if shape == 'Rectangle':
                rectangle_colors.append(h)
                num_rectangles += 1
            else:
                circle_colors.append(h)
                num_circles += 1

    result_circles = []
    result_rectangles = []

    while circle_colors:
        color1 = circle_colors.pop(0)
        group = [color1]
        for color2 in circle_colors.copy():
            if abs(color1 - color2) < 0.1:
                group.append(color2)
                circle_colors.remove(color2)
        result_circles.append(group)

    print("Группы по оттенкам кругов")
    for g in result_circles:
        print(len(g))

    while rectangle_colors:
        color1 = rectangle_colors.pop(0)
        group = [color1]
        for color2 in rectangle_colors.copy():
            if abs(color1 - color2) < 0.1:
                group.append(color2)
                rectangle_colors.remove(color2)
        result_rectangles.append(group)

    print("Группы по оттенкам прямоугольников")
    for g in result_rectangles:
        print(len(g))

    num_figures = num_rectangles + num_circles

    print("Общее количество фигур:", num_figures)
    print("Количество прямоугольников:", num_rectangles)
    print("Количество кружочков:", num_circles)

count_figures_by_color("balls_and_rects.png")
