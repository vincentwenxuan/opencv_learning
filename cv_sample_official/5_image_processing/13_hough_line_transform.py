# We will see how to use it detect lines in an image
# Hough Transform is a popular technique to detect any shape,
# if you can represent that shape in mathematical form.
# It can detect the shape even if it is broken or distorted a little bit.

# A good explanation of Hough can be found
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html#py-hough-lines

# Functions: cv2.HoughLines(), cv2.HoughLinesP()



import cv2
import numpy as np

img = cv2.imread('../images/wrapped_paper.png')
img_copy = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Hough Transform needs Binary Image, so we do an edge detection
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# ====== Hough Transforms
# 2nd and 3rd is the rho and theta accuracy, 4th is the vote threshold(could be seen as the min line length)
# return value is a list of rho, theta tuple
lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)  # 1 pixel, and 1 degree accuracy

for i in range(lines.shape[0]):
    rho, theta = lines[i, 0, :]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('image', img)
cv2.waitKey(0)

# ======= Probablistic Hough transform
# Standard Hough Transform is SLOW, it takes a lot of computation
# Probablistic version takes only a random set of points

# minLineLength: Minimum length of line. Line segments shorter than this are rejected.
# maxLineGap: Maximum allowed gap between line segments to treat them as single line.
minLineLength = 200
maxLineGap = 30  # the discontimg_copyinuity allowed in a line
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)

for i in range(lines.shape[0]):
    x1, y1, x2, y2 = lines[i, 0, :]
    cv2.line(img_copy, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.imshow('image', img_copy)
cv2.waitKey(0)
