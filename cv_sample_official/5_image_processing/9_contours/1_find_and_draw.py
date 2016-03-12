# The contours are a useful tool for shape analysis and object detection and recognition.
# ==> For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
# ==> findContours function modifies the source image.
# ==> In OpenCV, remember, object to be found should be white and background should be black.

# Functions: cv2.findContours(), cv2.drawContours()

import numpy as np
import cv2

# ====== Thresholding:
img = cv2.imread('../../images/tetris_blocks.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold, thresholded_img = cv2.threshold(imgray, 222, 255, cv2.THRESH_BINARY_INV)

# ====== Finding contours:
# return value "contours" is python list of ALL contours in image, each one is a list of coordinates
# argument "thresholded_img" is the image, 2nd is contour retrieval mode, 3rd is contour approximation method
# popular approximate are CHAIN_APPROX_NONE(no approximate) and CHAIN_APPROX_SIMPLE
_, contours, hierarchy = cv2.findContours(thresholded_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# ====== Draw contours:
# 1st is the image you want to draw, 2nd is the contours, 3rd the which contour to draw(-1 to draw all),
# 4th 5th is the color and thickness
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
cv2.imshow('ss', img)
cv2.waitKey(0)

# or you can draw a specific contour
a_cnt = contours[2]

cv2.drawContours(imgray, [a_cnt], 0, (0, 0, 255), 3)
cv2.imshow('ss', imgray)
cv2.waitKey(0)


