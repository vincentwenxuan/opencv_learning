import cv2
import numpy as np

# ====== Saturated property of OpenCV, better to use OpenCV version
x = np.uint8([250])
y = np.uint8([10])

print cv2.add(x, y)
print x + y

# ====== image blending

img1 = cv2.imread('../images/opencv_logo.png')
img2 = cv2.imread('../images/lenna.png')

img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))

img_blended = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)

cv2.imshow('blended', img_blended)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ====== Bitwise operation, masking
img1_logo = cv2.resize(img1, (100, 100))
img2_lenna = img2

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img1_logo.shape
roi = img2_lenna[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img1gray = cv2.cvtColor(img1_logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img1gray, 150, 255,
                          cv2.THRESH_BINARY)  # second arg is the threshold, third is the value given to high
mask_inv = cv2.bitwise_not(mask)  # inverse mask

# Now black-out the area of logo in ROI
img2_bg = cv2.bitwise_and(roi, roi, mask=mask)

# Take only region of logo from logo image.
img1_fg = cv2.bitwise_and(img1_logo, img1_logo, mask=mask_inv)

# add the two bg and fg and place it back
dst = cv2.add(img1_fg, img2_bg)
img2_lenna[0:rows, 0:cols] = dst

cv2.imshow('branded', img2_lenna)
cv2.waitKey(0)