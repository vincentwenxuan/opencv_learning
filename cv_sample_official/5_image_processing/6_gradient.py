# There are two main image gradient algorithm: Sobel(1st order) and Laplacian(2nd order)
# Laplacian is more sensitive to noise, Sobel needs to apply twice

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/wrapped_paper.png', 0)

# cv2.CV_8U represent the 'depth' of returned image(i.e. date type of pixels)
laplacian = cv2.Laplacian(img, cv2.CV_8U, ksize=5)


# NOTE that the gradient value could be positive and negative
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
sobely = np.absolute(sobely)


plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()
