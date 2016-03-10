# Functions: cv2.Canny()

# Canny edge detection can be divided into 4 steps:
# 1.Noise Reduction: noise removed by a 5*5 gaussian by default
# 2.Find Gradient: gradient magnitude and angle
# 3.Non-maximum Suppression: edge would be a single line
# 4.Edge-linking: pixels between two threshold would be linked to edges

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/lenna.png', 0)
edges = cv2.Canny(img, 100, 200) # image, threshold_min, threshold_max


plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
