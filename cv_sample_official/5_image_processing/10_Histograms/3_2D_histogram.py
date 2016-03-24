# We considering Hue and Saturation as 2D(compare to grayscale in the last case)
# Function: cv2.calcHist()


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../../images/lenna.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# ====== Calculate histogram
# NOTE that the 2nd argument is now [0,1] to indicate first and second(h ans s) in image
# 4th is [180 256] indicate the bin count to be 180 and 256 respectively
# 5th is [0,180,0,256] represents the scale
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

# ====== cv plot version
cv2.imshow('hist', hist)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ====== matlab plot version gives you color value so that we know which color we have
plt.imshow(hist, interpolation='nearest')
plt.show()
