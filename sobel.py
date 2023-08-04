import numpy as np
import cv2 as cv

img = cv.imread('img.jpeg',cv.IMREAD_GRAYSCALE)

laplacian = cv.Laplacian(img, cv.CV_64F)
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
sobel = cv.Sobel(img, cv.CV_64F, 1, 1, ksize=5)

print("input type: ",img.dtype)
print("laplacian type: ", laplacian.dtype)
print('Sobel x type: ', sobelx.dtype)
print('Sobel y type: ', sobely.dtype)

laplacian = cv.normalize(laplacian, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
sobelx = cv.normalize(sobelx, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
sobely = cv.normalize(sobely, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
sobel = cv.normalize(sobel, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)


cv.imwrite('laplacian.png', laplacian)
cv.imwrite("sobelx.png", sobelx)
cv.imwrite("sobely.png",sobely)
cv.imwrite("sobel.png",sobel)
