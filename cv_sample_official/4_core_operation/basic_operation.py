import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("../images/lenna.png")
assert isinstance(img, np.ndarray)

# ======== Accessing pixels

my_pixel = img[100, 100]
print my_pixel

my_redpixel = img[100, 100, 2]
print my_redpixel

# ====== Better way to access a single value

print img.item(100, 100, 2)

img.itemset((100, 100, 2), 250)
print img.item(100, 100, 2)


# ======= Property of an image
print "Shape of image:", img.shape

print "Total number of values in image:", img.size

print "Image data type: ", img.dtype

# ======= ROI

cv2.imshow('image', img)
cv2.waitKey(1500)
cv2.destroyAllWindows()

face = img[200:380, 200:360]
cv2.imshow('face', face)
cv2.waitKey(1500)

# ====== OpenCV splitting and merging Channels

b, g, r = cv2.split(img)

cv2.imshow('image', b)
cv2.waitKey(1500)

img = cv2.merge((b, g, r))

print img[:, :, 0]



