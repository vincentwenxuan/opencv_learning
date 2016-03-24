# matching the similarity of two shapes(important in recognition)
# Function: cv2.matchshapes()
# this function uses hu-moment, can compare two shapes in different rotation, displace, and scale

# return value is float, the smaller the better



import cv2
import numpy as np


img = cv2.imread('../../images/tetris_blocks.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, threshed_img = cv2.threshold(img_gray, 233, 255, 0)

_, contours, hierarchy = cv2.findContours(threshed_img, 2, 1)
cnt1 = contours[5]
cnt2 = contours[6]

# the 1st 2nd arguments are contours, 3rd is method, 4th is not available now
ret = cv2.matchShapes(cnt1, cnt2, 1, 0)
print ret

img = cv2.drawContours(img, contours, 6, (0, 0, 0), 2)
img = cv2.drawContours(img, contours, 5, (0, 0, 0), 2)

cv2.imshow('image', img)
cv2.waitKey(0)

