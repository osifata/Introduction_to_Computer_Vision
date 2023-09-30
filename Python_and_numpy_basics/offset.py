import numpy as np


def coordinates(name):
    image = np.loadtxt(name, skiprows=2)
    for y in range(1, image.shape[0] - 1):
        for x in range(1, image.shape[1] - 1):
            if image[y, x] == 1:
                return x, y


def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 +
            (p1[1] - p2[1]) ** 2) ** 0.5


x1, y1 = coordinates('img/img1.txt')
x2, y2 = coordinates('img/img2.txt')
offset_by_x = x2 - x1
offset_by_y = y2 - y1
vector_offset = distance([x1, y1], [x2, y2])

print("Смещение по x: ", offset_by_x, " Смещение по y: ", offset_by_y)
print("Векторное смещение", vector_offset)
