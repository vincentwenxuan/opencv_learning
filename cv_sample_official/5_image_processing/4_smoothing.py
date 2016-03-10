# There 4 main kinds of bluring: Averaging, Median, Gaussian, and Bilateral
# Functions: cv2.filter2D()

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/opencv_black.png')

# ====== 2D Convolution filtering
kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

# ====== Bluring (Averaging)
blur = cv2.blur(img, (15, 15))

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

# ====== Gaussian Bluring
# NOTE that the 3rd arg is the standard deviation, when gives 0, it will be caculated from the kernel size
blur = cv2.GaussianBlur(img, (15, 15), 0)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Gaussian Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

# ====== Median Bluring: very effective in reducing salt-and-pepper noise
# NOTE that interesting thing is, the center point will ALWAYS some pixel from the image(instead of a new value)

img_median = cv2.imread('../images/opencv_noisy.png')
median = cv2.medianBlur(img_median, 11)

plt.subplot(121), plt.imshow(img_median), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(median), plt.title('Median Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

# ====== Bilateral Filtering: Very Effective to reduce noise while KEEPING the edges
img_bilateral = cv2.imread('../images/bilateral_blur.png')

blur = cv2.bilateralFilter(img_bilateral, 23, 75, 75)

plt.subplot(121), plt.imshow(img_bilateral), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Bilateral Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


