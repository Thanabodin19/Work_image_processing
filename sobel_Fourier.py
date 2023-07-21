import numpy as np
import cv2 as cv
from scipy import fftpack

img = cv.imread('img.jpeg',cv.IMREAD_GRAYSCALE)


#สร้าง Sobel Filter แบบ Horizontal หรือ Vertical อย่างใดอย่างหนึ่งใน Spatial Domain
kernel = np.array([[2,2,4,2,2],
                    [1,1,2,1,1],
                    [0,0,0,0,0],
                    [-1,-1,-2,-1,-1],
                    [-2,-2,-4,-2,-2]])
sz = (img.shape[0] - kernel.shape[0], img.shape[1] - kernel.shape[1])  
kernel = np.pad(kernel, (((sz[0]+1)//2, sz[0]//2), ((sz[1]+1)//2, sz[1]//2)), 'constant')
kernel = np.fft.ifftshift(kernel)

#แปลงภาพ Input ให้อยู่ใน Frequency Domain ด้วย Fourier Transform
imgF = np.fft.fft2(img)


#แปลง Filter Sobel ให้อยู่ใน Frequency Domain ด้วย Fourier Transform
filF = np.fft.fft2(kernel)

# #นำภาพ Input และ Filter Sobel ใน Frequency Domain มาทำการคูณกันแบบจุดต่อจุด (Dot Product)
Dot_sobel = imgF*filF 

#แปลงภาพผลลัพธ์กลับมายัง Spatial Domain
dotInv = np.fft.ifft2(Dot_sobel)
dotReal = np.real(dotInv)

#เปรียบเทียบผลลัพธ์ที่ได้ระหว่างการทำ Filter Sobel ใน Spatial Domain และ Frequency Domain ว่าเหมือนกันหรือไม่

#function Sobel
sobel = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
sobel = cv.normalize(sobel, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
cv.imwrite("func_sobel.png",sobel)

#Fourire Sobel
dotInv = cv.normalize(dotReal, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
cv.imwrite('fourier_soble.png', dotInv)



