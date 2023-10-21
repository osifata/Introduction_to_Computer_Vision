import numpy as np
from skimage.morphology import (binary_erosion, binary_dilation, binary_closing, binary_opening)
from skimage.morphology import label

image = np.load("psnpy.txt")
labeled_all = label(image)
count_all = len(np.unique(labeled_all)) - 1
print("Общее количество фигур: ", count_all)

struct = np.ones((4, 6))
rect = binary_opening(image, struct)
labeled_rect = label(rect)
count_rect = len(np.unique(labeled_rect)) - 1
print("Количество прямоугольников: ", count_rect)

new_image = np.copy(image)
for i in np.unique(labeled_rect)[1:]:
    new_image[labeled_rect == i] = 0

struct_down = np.array([
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1]
])
struct_up = np.array([
    [1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
])
struct_left = np.array([
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
])
struct_right = np.array([
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
])

masks = [struct_up, struct_left, struct_down, struct_right]
for i, mask in enumerate(masks):
    ero = binary_erosion(new_image, mask)
    labeled = label(ero)
    count = len(np.unique(labeled)) - 1
    print("Количество объектов разных фигур:", count)
