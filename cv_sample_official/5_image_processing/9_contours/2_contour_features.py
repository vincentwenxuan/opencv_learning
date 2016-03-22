# We'll learn a set of functions in finding contour-like features
# Functions:
# cv2.moments(cnt)
# cv2.contourArea(cnt)
# cv2.arcLength(cnt,True)
# cv2.approxPolyDP(cnt,epsilon,True)
# cv2.convexHull()
# cv2.isContourConvex(cnt)
# cv2.boundingRect(cnt)    # (straight rectangle)
# cv2.minAreaRect(cnt)     # (rotatable rectangle)
# cv2.minEnclosingCircle(cnt)
# cv2.fitEllipse(cnt)
# cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)


import numpy as np
import cv2

img = cv2.imread('../../images/tetris_blocks.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ====== Image moments are a set of scalars caculated from confours that has some meaning(:D)
ret, thresholded_img = cv2.threshold(img_gray, 233, 255, 0)
_, contours, hierarchy = cv2.findContours(thresholded_img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[1]
M = cv2.moments(cnt)
print 'M', M

# ====== Contour area, compute the area from a specific contour
area = cv2.contourArea(cnt)
print 'Area:', area

# ====== Arc length(Perimeter), 2nd arg is whether its a closed contour
perimeter = cv2.arcLength(cnt, True)
print 'perimeter:', perimeter

# ====== Contour Approximation, make approximation and handle contour noise
# 2nd argument is maximum distance from contour to approximated contour, it's an accuracy parameter.
# a wise selection of epsilon is needed to get it right
# result is an apporximated contour
epsilon = 0.1 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)

img_cp = img.copy()
cv2.drawContours(img_cp, [approx], -1, (0, 0, 0), 2)
cv2.imshow('Approx', img_cp)
cv2.waitKey(0)

# ====== Convex Hull, similar to approximation but not the same
# hull = cv2.convexHull(points[, hull[, clockwise[, returnPoints]]
# 2nd is output(avoid it), 3rd is whether is clockwise, 4th is True return Points False return index

hull = cv2.convexHull(cnt)

img_cp = img.copy()
cv2.drawContours(img_cp, [hull], -1, (0, 0, 0), 2)
cv2.imshow('Convex', img_cp)
cv2.waitKey(0)

# ====== check Convexity
print 'convexity:', cv2.isContourConvex(cnt)

# ====== Straight bounding rect:
# x, y is the left top point and w, h is the width and height
x, y, w, h = cv2.boundingRect(cnt)

img_cp = img.copy()
img_cp = cv2.rectangle(img_cp, (x, y), (x + w, y + h), (0, 0, 0), 2)
cv2.imshow('Straight rect', img_cp)
cv2.waitKey(0)

# ====== Rotatable bounding rect:
rect = cv2.minAreaRect(cnt)  #
box = cv2.boxPoints(rect)  # box is the four corners(float)
box = np.int0(box)

img_cp = img.copy()
img_cp = cv2.drawContours(img_cp, [box], 0, (0, 0, 255), 2)
cv2.imshow('Rotatable rect', img_cp)
cv2.waitKey(0)

# ====== Minimum enclosing circle:
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)

img_cp = img.copy()
img_cp = cv2.circle(img_cp, center, radius, (0, 255, 0), 2)
cv2.imshow('enclosing circle', img_cp)
cv2.waitKey(0)

# ====== Minimum Enclosing Eclipse
ellipse = cv2.fitEllipse(cnt)

img_cp = img.copy()
img_cp = cv2.ellipse(img_cp, ellipse, (0, 255, 0), 2)
cv2.imshow('Enclosing Eclipse', img_cp)
cv2.waitKey(0)

# ====== Fitting a Line: (Well... )
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
img_cp = img.copy()
img_cp = cv2.line(img_cp, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)
cv2.imshow('Line', img_cp)
cv2.waitKey(0)