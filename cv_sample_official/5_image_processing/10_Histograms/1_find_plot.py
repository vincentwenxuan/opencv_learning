# So what is histogram ? You can consider
# histogram as a graph or plot, which gives you an
# overall idea about the intensity distribution of an image.
# It is a plot with pixel values (ranging from 0 to 255, not always)in X-axis and
# corresponding number of pixels in the image on Y-axis.

# Functions: cv2.calcHist(), np.histogram()



import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../../images/lenna.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1st argument is the image(could be gray or color) in []
# 2nd argument is channels, if it's a gray just pass 0, color you can pass 0, 1 or 2 to indicate the BGR
# 3rd argument is mask, to indicate ROI
# 4th is the bin count, represent how much segments in histgram
# 5th is the range
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# there is also a numpy version of finding histgram
# hist,bins = np.histogram(img.ravel(),256,[0,256])
# but is much slower(around 40X) than opencv, just stick to opencv


# ====== Ploting Using Matlibplot:

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()

# ====== Masking:


# create a mask
mask = np.zeros(img_gray.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img_gray, img_gray, mask=mask)

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
hist_mask = cv2.calcHist([img_gray], [0], mask, [256], [0, 256])

plt.subplot(221), plt.imshow(img_gray, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0, 256])

plt.show()
