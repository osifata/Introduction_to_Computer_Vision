import matplotlib.pyplot as plt
import numpy as np
from skimage.morphology import (binary_dilation)
from skimage.morphology import label
from skimage.measure import regionprops


def has_vline(arr):
    return 1. in arr.mean(0)

def reg(tmp):
    tmp_labeled = label(tmp)
    return regionprops(tmp_labeled)

def recognize(prop):
    euler_number = prop.euler_number
    if euler_number == -1:
        if has_vline(prop.image):
            return "B"
        else:
            return "8"
    elif euler_number == 0:
        tmp = prop.image.copy()
        tmp[-1, :] = 1
        tmp_props = reg(binary_dilation(tmp))
        tmp_euler = tmp_props[0].euler_number
        if tmp_euler == -1:
            return "A"
        elif tmp_euler == 1:
            return "*"
        else:
            if has_vline(prop.image):
                tmp = prop.image.copy()
                tmp_cent = tmp.shape[0] // 2
                tmp[tmp_cent, :] = 1
                tmp_props = reg(binary_dilation(tmp))
                tmp_euler = tmp_props[0].euler_number
                if tmp_euler == -1:
                    return "D"
                else:
                    return "P"
            else:
                return "0"
    else:
        if prop.image.mean() == 1:
            return "-"
        else:
            if has_vline(prop.image) and has_vline(prop.image.T):
                return "1"
            else:
                tmp = prop.image.copy()
                tmp[[0, -1], :] = 1
                tmp[:, [0, -1]] = 1
                tmp_props = reg(tmp)
                tmp_euler = tmp_props[0].euler_number
                if tmp_euler == -3:
                    return "X"
                elif tmp_euler == -1:
                    return "/"
                else:
                    if prop.eccentricity > 0.5:
                        return "W"
                    else:
                        return "*"
    return "_"


image = plt.imread("symbols.png")
image = image.mean(2)
image = image > 0

labeled = label(image)
count = len(np.unique(labeled)) - 1
print(count)

props = regionprops(labeled)
result = {}
for prop in props:
    symbol = recognize(prop)
    if symbol not in result:
        result[symbol] = 0
    result[symbol] += 1
print(result)

percent = ((1 - result.get("_", 0) / count) * 100)
print(percent, "%")

print()

plt.imshow(labeled)
plt.show()
