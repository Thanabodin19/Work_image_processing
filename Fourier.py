import numpy as np
import cv2 as cv

img = cv.imread('images.jpeg',cv.IMREAD_GRAYSCALE)

#cast data type to float 32 bit
img = img.astype(np.float32)

imgF = np.fft.fft2(img)

imgF = np.fft.fftshift(imgF)

imgReal = np.real(imgF)
imgIma = np.imag(imgF)
imgMag = np.sqrt(imgReal**2 + imgIma**2)
imgPhs = np.arctan2(imgIma, imgReal)

#inverse Fourier transform
imgRealInv = imgMag*np.cos(imgPhs)
imgImaInv = imgMag*np.sin(imgPhs)

imgFInv = imgRealInv + imgImaInv*1j

imgFInv = np.fft.ifftshift(imgFInv)
imgInv = np.fft.ifft2(imgFInv)

imgInv = np.real(imgInv)
imgInv = imgInv.astype(np.uint8)

cv.imwrite("input.png",img)
cv.imwrite('output.png', imgInv)

imgMag = np.log(1+imgMag)
imgMag = cv.normalize(imgMag, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
cv.imwrite("magnitude.png", imgMag)
