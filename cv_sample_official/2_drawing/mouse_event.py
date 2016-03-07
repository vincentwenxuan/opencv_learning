import cv2
import numpy as np


# mouse callback function
# the callback takes exactly 5 arguments
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (255, 0, 0), -1)
        print "hello world"


# Create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:  # ESC key
        break

cv2.destroyAllWindows()
