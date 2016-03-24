# We will learn the concepts of histogram equalization and use it to improve the contrast of our images.

# histogram equalization is a way to enhance contrast



import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../../images/lenna.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

equ = cv2.equalizeHist(img_gray)
stitched = np.hstack((img_gray,equ)) #stacking images side-by-side

cv2.imshow('img', stitched)
cv2.waitKey(0)


# ====== BUT this gloabal equalization is not ideal(make bright things brighter)
# here is an algorithm called CLAHE (Contrast Limited Adaptive Histogram Equalization)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img_gray)

cv2.imshow('img', cl1)
cv2.waitKey(0)

