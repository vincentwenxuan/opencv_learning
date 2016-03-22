# A set of HOW-TO of getting contour properties
# 1. Aspect Ratio
# 2. Extent
# 3. Solidity
# 4. Equivalent Diameter
# 5. Orientation
# 6. Mask and Pixel Points
# 7. Maximum Value, Minimum Value and their locations
# 8. Mean Color or Mean Intensity
# 9. Extreme Points


import numpy as np
import cv2

img = cv2.imread('../../images/tetris_blocks.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresholded_img = cv2.threshold(img_gray, 233, 255, 0)
_, contours, hierarchy = cv2.findContours(thresholded_img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[1]

# ======= 1.Aspect Ratio:
x, y, w, h = cv2.boundingRect(cnt)
aspect_ratio = float(w) / h
print 'aspect_ratio', aspect_ratio

# ====== 2. Extent: is the ratio of contour area to bounding rectangle area.
area = cv2.contourArea(cnt)
x, y, w, h = cv2.boundingRect(cnt)
rect_area = w * h
extent = float(area) / rect_area
print 'extent', extent

# ====== 3. Solidity: is the ratio of contour area to its convex hull area.
area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area) / hull_area
print 'solidity', solidity

# ====== 4. Equivalent Diameter
area = cv2.contourArea(cnt)
equi_diameter = np.sqrt(4 * area / np.pi)
print 'equi_diameter', equi_diameter

# ====== 5. Orientation
(x, y), (MA, ma), angle = cv2.fitEllipse(cnt)
print 'Major axis(length):', MA
print 'Minor axie(length):', ma
print 'Angle', angle

# ====== 6. Mask
# use contour to make a mask
# the two way to find pixelpoints are the same
# but Numpy version has to transpose since its in rows,columns
mask = np.zeros(img_gray.shape, np.uint8)
cv2.drawContours(mask, [cnt], 0, 255, -1)  # NOTE: -1 means fill, so it's showing the image within contour
pixelpoints = np.transpose(np.nonzero(mask))
# pixelpoints = cv2.findNonZero(mask)
cv2.imshow('mask', mask)
cv2.waitKey(0)

# ====== 7.Maximum Value, Minimum Value and their locations
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img_gray, mask=mask)
print 'min_val:', min_val
print 'max_val:', max_val
print 'min_loc:', min_loc

# ====== 8. Mean value:(Note that the img can be colored and mean with be with each channel)
mean_val = cv2.mean(img, mask=mask)
print "mean_val:", mean_val

# ====== 9. Extreme points:
leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])  # NOTE that the 0 represent x coordinate, so the minimum of it is left
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
print 'leftmost:', leftmost