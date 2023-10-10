import numpy as np
import cv2 as cv

def linear(r,theta):
    
    for i in range(r):
        x = int(abs(i * np.cos(theta)))
        y = int(abs(i * np.sin(theta)))
        kernel[x,y] = 255
    return kernel
       

img = cv.imread("66280.jpg",cv.IMREAD_GRAYSCALE)
size = 50
kernel = np.zeros([size,size], np.uint8)
theta = 45

linear(size,theta)
norm = kernel.sum()

output = cv.filter2D(img, -1, kernel/(norm), borderType = cv.BORDER_REFLECT)

cv.imwrite("input.png",img)
cv.imwrite("output.png",output)
# cv.waitKey(0)
# cv.destroyAllWindows()