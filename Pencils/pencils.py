import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
from skimage.morphology import label
from skimage.measure import regionprops

objects_len = []
count = 0

for i in range(1, 13):
    image = plt.imread(f"images/img_{i}.jpg")
    image = image.mean(2)
    cropped_image = image[:, 50:-50]
    thresh = threshold_otsu(cropped_image)
    binary = cropped_image <= thresh * 1.05
    labeled = label(binary)
    regions = regionprops(labeled)
    for reg in regions:
        length = reg.axis_major_length
        objects_len.append(length)

max_len = max(objects_len)
for i in objects_len:
    if max_len - i < 300:
        count += 1

print("Общее количество карандашей: ", count)
