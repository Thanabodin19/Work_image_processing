import cv2 as cv
import random
import numpy as np

def salt_papper_noise(img):

    density_salt = 0.1
    density_pepper = 0.1

    number_of_white_pixel = int(density_salt * (img.shape[0] * img.shape[1]))

    for i in range(number_of_white_pixel):
        y_coord = random.randint(0, img.shape[0] - 1)
        x_coord = random.randint(0, img.shape[1] - 1)
        img[y_coord, x_coord] = 255


    number_of_black_pixel = int(density_pepper * (img.shape[0] * img.shape[1]))

    for i in range(number_of_black_pixel):
        y_coord = random.randint(0, img.shape[0] - 1)
        x_coord = random.randint(0, img.shape[1] - 1)
        img[y_coord, x_coord] = 0
    


def denoise(image1, image2):
    blur = 1
    max_ssim = 0
    
    for _ in range(10):
        img_blur = cv.medianBlur(image2, blur)
        cv.imwrite("img_blur{}.png".format(blur),img_blur)
        ssim = SSIM(image1,img_blur)
        mse = np.mean((image1 - img_blur) ** 2)
        print(mse)
        if ssim > max_ssim and mse < 1:
            max_ssim = ssim
            size_blur = blur
        blur += 2

    img_denoise = cv.medianBlur(image2, size_blur)
    return img_denoise

    

def SSIM(image1, image2):
    image1 = image1.astype(np.float64)
    image2 = image2.astype(np.float64)

    image1 = image1/255
    image2 = image2/255

    K1 = 0.01
    K2 = 0.03
    L = 1

    mu1 = np.mean(image1)
    mu2 = np.mean(image2)

    sigma1_sq = np.var(image1)
    sigma2_sq = np.var(image2)
    sigma12 = np.cov(image1.flatten(), image2.flatten())[0, 1]

    C1 = (K1 * L) ** 2
    C2 = (K2 * L) ** 2
    numerator = (2 * mu1 * mu2 + C1) * (2 * sigma12 + C2)
    denominator = (mu1 ** 2 + mu2 ** 2 + C1) * (sigma1_sq + sigma2_sq + C2)

    ssim_score = numerator / denominator

    return ssim_score

image = cv.imread('images.jpeg',cv.IMREAD_GRAYSCALE)
image_compare = cv.imread('images.jpeg',cv.IMREAD_GRAYSCALE)
salt_papper_noise(image)
output = denoise(image_compare, image)
cv.imwrite("img _denoise.png",output)
cv.imwrite("img _noise.png",image)

cv.imshow("image_in", image_compare)
cv.imshow("noise",image)
cv.imshow("denoise",output)
cv.waitKey(0)
cv.destroyAllWindows()