import cv2
import numpy as np
import matplotlib.pyplot as plt

BLUE = [255, 0, 0]

img1 = cv2.imread('../images/opencv_logo.png')
img1 = cv2.resize(img1, (200, 200))

# ====== cv2.copyMakeBorder function: there are 5 options to make border(padding)
replicate = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=BLUE)

# ====== matplotlib library usage
plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
plt.show()

# ====== compare to cv's imshow -- RGB BGR
cv2.imshow("image", constant)
cv2.waitKey(0)
