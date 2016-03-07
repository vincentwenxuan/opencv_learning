import numpy as np
import cv2

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# arg: image MAT, starting point, ending point, color, thickness
# return the drawed image
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# rect drawing:  left-top point and right-bottom point
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# circle drawing:
# NOTE: -1 means fill (instead of a thickness)
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

# ellipse
# arg: center, major minor axis, angle, start and end angle, color, thickness
img = cv2.ellipse(img, (256, 256), (100, 50), 30, 0, 90, (0, 0, 244), -1)

# polygon
# NOTE that how pts are shaped
#  arg: image, points, isClosed?, color
pts = np.array([[20, 10], [40, 60], [140, 40], [100, 20]], dtype=np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (0, 255, 255))

# text
# arg: image, text string, position, font, size, color, thickness, line style
font = cv2.FONT_HERSHEY_SIMPLEX
text_str = 'OpenCV'
cv2.putText(img, text_str, (10, 500), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
