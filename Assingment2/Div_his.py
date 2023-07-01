import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

#https://github.com/Devyanshu/image-split-with-overlap ################
def start_points(size, split_size, overlap=0):
    points = [0]
    stride = int(split_size * (1-overlap))
    counter = 1

    while True:
        pt = stride * counter
        if pt + split_size >= size:
            if split_size == size:
                break
            points.append(size - split_size)
            break
        else:
            points.append(pt)  
        counter += 1
    return points
######################################################################


def Split_img(img, X_points, Y_points, split_height, split_width, mean, gamma_high, gamma_low):
    count_pic = 0
    name = 's'
    frmt = 'jpeg'
    count2 = 0
    ar0255 = np.arange(0,256)/255
    h_cut = split_height//3
    w_cut = split_width//3
    
    banner = Image.new('RGBA',(img_w,img_h))

    for i in Y_points:
        count = 0
        for j in X_points:
            split = img[i:i+split_height, j:j+split_width]
            img_gray = cv.cvtColor(split, cv.COLOR_BGR2GRAY)
            img_eq = cv.equalizeHist(img_gray)
            average = np.mean(img_eq)//255

            if average < mean:
                gamma_corrected = (split/255)**gamma_low
            else:
                gamma_corrected = (split/255)**gamma_high
            gamma_corrected = gamma_corrected*255
            img_out = np.array(gamma_corrected, dtype='uint8')
            
            block = img_out[h_cut:h_cut*2, w_cut:w_cut*2]
            cv.imwrite('picture/{}_{}.{}'.format(name, count_pic, frmt), block)
            c_img = Image.open('picture/{}_{}.{}'.format(name, count_pic, frmt))

            if i==0 and j==0:
                banner.paste(c_img,(0,0))
            else:
                banner.paste(c_img,(j-((h_cut//2)*count),i-((w_cut//2)*count2)))
            
            count += 1
            count_pic += 1
        count2 += 1          
    return banner

path_to_img = "66283.jpg"
img = cv.imread(path_to_img)
img_input = Image.open(path_to_img)
img_h, img_w, _ = img.shape
split_width = 90
split_height = 90
mean = 0.5
gamma_low = 0.3 
gamma_high = 1.3

X_points = start_points(img_w, split_width, 0.5)
Y_points = start_points(img_h, split_height, 0.5)

img_output = Split_img(img, X_points, Y_points, split_height, split_width, mean, gamma_high, gamma_low)
img_input.show()
img_output.show()

