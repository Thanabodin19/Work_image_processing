import cv2
import numpy as np

def Circle_Detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    wide = cv2.Canny(blurred, 200, 255)
    w, h, _ = image.shape
    for x in range(0,h,3):
        for y in range(0,w,3):
            edge = wide[y,x]
            
            if edge >= 255:
                cv2.circle(image, (x, y), 60, (0, 255, 0), 1)
                cv2.circle(img,(x,y),2,(0,0,255),3)
    cv2.imwrite("output_circle.png", image)
    cv2.imshow('detected',wide)
    cv2.imshow('detected circles',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = "ci.png"
img = cv2.imread(image_path)
Circle_Detection(img)