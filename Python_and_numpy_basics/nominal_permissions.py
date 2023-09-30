import numpy as np


def nominal_permissions(name):
    with open(name) as text_file:
        lines = text_file.readlines()
    mm = int(lines[0])
    array = np.loadtxt(name, skiprows=2)
    max_pixels = 0
    count_pixels = 0
    for a in array:
        if a.any() == 1:
            count_pixels += 1
        else:
            if count_pixels > max_pixels:
                max_pixels = count_pixels
            count_pixels = 0
    if max_pixels != 0:
        permission = mm / max_pixels
    else:
        permission = 0
    return permission


print("Первая фигура: ", nominal_permissions('figures/figure1.txt'))
print("Вторая фигура: ", nominal_permissions('figures/figure2.txt'))
print("Третья фигура: ", nominal_permissions('figures/figure4.txt'))
print("Четвертая фигура: ", nominal_permissions('figures/figure5.txt'))
print("Пятая фигура: ", nominal_permissions('figures/figure6.txt'))
