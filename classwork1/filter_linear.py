import numpy as np
import cv2 as cv

img = cv.imread("66280.jpg",cv.IMREAD_GRAYSCALE)

filterSize = 15
kernel = np.ones((filterSize,filterSize), np.float32)/(filterSize**2)
print(kernel)
output = cv.filter2D(img, -1, kernel, borderType = cv.BORDER_REFLECT)

cv.imwrite("a.png",img)
cv.imwrite("n.png",output)