# Change color spaces like BGR, HSV, Gray
# HSV is very important, stand for Hue(0~179), Saturate(0~255), Value(0~255)
# Functions: cv2.cvtColor(), cv2.inRange()


import cv2
import numpy as np

# ====== ALL convert available in opencv
convert_flag = [i for i in dir(cv2) if i.startswith('COLOR_')]
print convert_flag

# ====== Find HSV value of a specific color!
green = np.uint8([[[0, 255, 0 ]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print "HSV representing 'Green' is:", hsv_green


# ====== Object tracking based on HSV color space
cap = cv2.VideoCapture(0)

while 1:

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Threshold the HSV image to get only blue colors
    # cv2.inRange() function, used to creat the thresholded mask

    mask = cv2.inRange(hsv, lower_blue, upper_blue)  # mask with value 0 or 255

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    #cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()





