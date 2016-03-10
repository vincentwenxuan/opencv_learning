# Geometry transformations: Scale ,Rotate, Affine, Perspective
# Functions: cv2.resize()  cv2.getRotationMatrix2D() cv2.getAffineTransform()
#    cv2.warpAffine() cv2.getAffineTransform()  cv2.getPerspectiveTransform()
#    cv2.warpPerspective()

import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_img(image):
    cv2.imshow('lenna', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('../images/lenna.png')

# ======= Scaling: resizing the image

# These two are equivalent:
# fx,fy represents the scaling factors
res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# 2nd argument represents the target resolution
height, width = img.shape[:2]
res = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
display_img(res)

# ======= Translation: shift the image

rows, cols, _ = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])  # Matrix including the shift x y
dst = cv2.warpAffine(img, M, (cols, rows))  # last argument is the dst size of image
display_img(dst)

# ======= Rotation: Rotate refer to a center

rows, cols, _ = img.shape
# cv2.getRotationMatrix2D(center of rotation, rotation angle, scale)
# opencv use a special rotation matrix that include info of center and scale
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))
display_img(dst)

# ====== Affine Transformation: Three point affine(starting 3pts to target 3pts)
rows, cols, ch = img.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)  # automatically get 3pts Affine

dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()


# ====== Perspective Transformation: Four Point perspective(starting 4pts ==> target 4pts)
rows, cols, ch = img.shape

pts1 = np.float32([[100, 100], [400, 100], [100, 400], [400, 400]])
pts2 = np.float32([[150, 100], [350, 100], [50, 400], [450, 300]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()

