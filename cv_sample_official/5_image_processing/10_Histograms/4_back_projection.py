# === Back Projection is useful in image segmentation or finding objects of interest in an image.
# What is back projection??
# In simple words:
# We specify an object in the image, calculate its histogram
# Through Back Projection we have the probability of each pixel belonging to this object
# then we make a threshold and get the region we want

# Function: cv2.calcBackProject().


import cv2
import numpy as np

roi = cv2.imread('../../images/apple_ROI.png')
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

target = cv2.imread('../../images/apple.png')
hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

# calculating object histogram
roihist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

# normalize histogram and apply backprojection
# 1st arg source, 2nd arg dst, 3rd alpha(lower range in this case), 4th beta(upper range), 5th norm type
cv2.normalize(roihist, roihist, 0, 255, cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)

# Now convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
# 1st source, 2nd depth(data type), 3rd kernel, 4th dst image
cv2.filter2D(dst, -1, disc, dst)  # -1 means output image will have the same depth as the source

# threshold and binary AND
ret, thresh = cv2.threshold(dst, 30, 255, 0)
thresh = cv2.merge((thresh, thresh, thresh))
res = cv2.bitwise_and(target, thresh)

res = np.vstack((target, thresh, res))
cv2.imshow('image', res)
cv2.waitKey(0)
