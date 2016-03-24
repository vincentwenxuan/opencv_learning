# You'll learn how to find objects in an image using Template Matching
# It simply slides the template image over the input image (as in 2D convolution)
# and compares the template and patch of input image under the template image.

# NOTE that the template and target should be SAME size

# Functions: cv2.matchTemplate(), cv2.minMaxLoc()


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/lenna.png', 0)
img2 = img.copy()
template = cv2.imread('../images/lenna_template.png', 0)
# NOTE: that the template and target should be SAME size
template = cv2.resize(template, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# We can see that TM_CCORR is not good(I don't know why as the website said so either)
for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()
