# Morphological transformation: Erosion, Dilate and other
# Functions: cv2.erode(), cv2.dilate(), cv2.morphologyEx()


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../images/j.png', 0)

# ====== Erosion: (Literally)
# in general, kernel size high or iteration high will erode more
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

plt.subplot(121), plt.imshow(img, cmap='Greys'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(erosion, cmap='Greys'), plt.title('Erosion')
plt.xticks([]), plt.yticks([])
plt.show()

# ====== Dilation: (Literal)
dilation = cv2.dilate(img, kernel, iterations=1)

plt.subplot(121), plt.imshow(img, cmap='Greys'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dilation, cmap='Greys'), plt.title('Dilation')
plt.xticks([]), plt.yticks([])
plt.show()

# ====== Opening(Can be seen as Dilate and Erode) : Remove noise
img = cv2.imread('../images/j_opening.png', 0)

opening = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.subplot(121), plt.imshow(img, cmap='Greys'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(opening, cmap='Greys'), plt.title('Opening')
plt.xticks([]), plt.yticks([])
plt.show()


# ====== Closing(Can be seen as Erode and Dilate) : remove internal holes
img = cv2.imread('../images/j_closing.png', 0)

opening = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.subplot(121), plt.imshow(img, cmap='Greys'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(opening, cmap='Greys'), plt.title('Closing')
plt.xticks([]), plt.yticks([])
plt.show()


# ====== Kernel creation: it's like the paint brush shape creation

print cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

print cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

print cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))