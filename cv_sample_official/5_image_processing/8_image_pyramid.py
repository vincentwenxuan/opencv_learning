# image pyramid could be used as stitching and blending, has two kinds: 1) Gaussian Pyramid and 2) Laplacian Pyramids
# Functions: cv2.pyrUp(), cv2.pyrDown()

import cv2
import numpy as np
import matplotlib.pyplot as plt


def display_img(img, dis_name='image'):
    assert isinstance(dis_name, basestring)
    cv2.imshow(dis_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ====== original image
img = cv2.imread('../images/lenna.png')
display_img(img, 'original')
print img.shape

# ====== pyrdown would make the picture smaller
down1 = cv2.pyrDown(img)
display_img(down1, 'down1')
print down1.shape

down2 = cv2.pyrDown(down1)
display_img(down2, 'down2')
print down2.shape

down3 = cv2.pyrDown(down2)
display_img(down3, 'down3')
print down3.shape

# ====== pyrdown would make the picture bigger, note that it will NOT restore the image as you will see
up1 = cv2.pyrUp(down3)
display_img(up1, 'down1')
print up1.shape

up2 = cv2.pyrUp(up1)
display_img(up2, 'down1')
print up2.shape

up3 = cv2.pyrUp(up2)
display_img(up3, 'down1')
print up3.shape

# ====== image blending example

A = cv2.imread('../images/apple.png')
B = cv2.imread('../images/orange.png')
A = cv2.resize(A, (512, 512))
B = cv2.resize(B, (512, 512))

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in xrange(5, 0, -1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i - 1], GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in xrange(5, 0, -1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i - 1], GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols / 2], lb[:, cols / 2:]))
    LS.append(ls)

    # now reconstruct
ls_ = LS[0]
for i in xrange(1, 6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack((A[:, :cols / 2], B[:, cols / 2:]))

plt.subplot(121), plt.imshow(real), plt.title('Direct_blending')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(ls_), plt.title('Pyramid_blending')
plt.xticks([]), plt.yticks([])
plt.show()
