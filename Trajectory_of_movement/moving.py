import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops


def find_center(regions, moving_fig1, moving_fig2):
    regions.sort(key=lambda x: x.area, reverse=True)
    moving_fig1.append(regions[0].centroid)
    moving_fig2.append(regions[1].centroid)
    return moving_fig1, moving_fig2


file_paths = ["out/h_{}.npy".format(i) for i in range(1, 100)]

moving_fig1 = []
moving_fig2 = []

for file_path in file_paths:
    image = np.load(file_path)
    labeled = label(image)
    regions = regionprops(labeled)
    if len(regions) > 0:
        find_center(regions, moving_fig1, moving_fig2)
    else:
        print("No different figures")

moving_fig1 = np.array(moving_fig1)
moving_fig2 = np.array(moving_fig2)
plt.plot(moving_fig1[:, 1], moving_fig1[:, 0], '-o', c='red', label='Trajectory 1')
plt.plot(moving_fig2[:, 1], moving_fig2[:, 0], '-o', c='blue', label='Trajectory 2')

plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trajectories of Objects')
plt.show()
