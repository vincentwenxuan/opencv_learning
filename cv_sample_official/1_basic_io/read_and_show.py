import numpy as np
import cv2


file_name = '../images/lenna.png'

img = cv2.imread(file_name, 1)
img = cv2.resize(img, (1024, 768))
cv2.imshow("image", img)
k = cv2.waitKey(0) & 0xff

if k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('lenna.png',img)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()