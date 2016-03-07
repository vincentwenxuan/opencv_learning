# function: cv2.getTickCount, cv2.getTickFrequency
# Also, python provides module like "time" and "profile" very useful to see performance

import cv2

img1 = cv2.imread('../images/lenna.png')

e1 = cv2.getTickCount()

for i in xrange(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)

e2 = cv2.getTickCount()
cpu_clicks = e2 - e1
time = cpu_clicks/cv2.getTickFrequency()

print cpu_clicks
print time


# ====== optimization (It is enabled by default)
print cv2.useOptimized()

e1 = cv2.getTickCount()
ret = cv2.medianBlur(img1, 49)
e2 = cv2.getTickCount()
print (e2-e1)/cv2.getTickFrequency()


cv2.setUseOptimized(False)
e1 = cv2.getTickCount()
ret = cv2.medianBlur(img1, 49)
e2 = cv2.getTickCount()
print (e2-e1)/cv2.getTickFrequency()


# ===== Tips:
"""
1. Avoid using loops in Python as far as possible, especially double/triple loops etc.
2. Vectorize the algorithm/code to the maximum possible extent because Numpy and OpenCV are optimized for vector operations.
3. Exploit the cache coherence.
4. Never make copies of array unless it is needed. Try to use views instead. Array copying is a costly operation.

Still slow: try Cython
"""