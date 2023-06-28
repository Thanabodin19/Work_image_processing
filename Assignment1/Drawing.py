import numpy as np
import cv2 as cv

img = np.zeros([200,300], np.uint8)

def Line():
    for y in range(0,125):
        for x in range(0,2):
            img[y,x] = 255

# drawing circle
# cv.circle(img,(150,100), 50, (255,255,255), -1)
def Circle(a,b,r):
    # a, b = 150,100
    # r = 50
    for y in range(b-r-2,b+r+2):
        for x in range(a-r-2,a+r+2):
            if ((x-a)**2 + (y-b)**2 - r**2) < 1**2:
                img[y,x] = 255

# drawing circle border
# cv.circle(img,(150,100), 50, (255,255,255), 3)
def Circle_border(a,b,r,d):
    # a, b = 150,100
    # r = 50
    for y in range(b-r-2,b+r+2):
        for x in range(a-r-2,a+r+2):
            if abs((x-a)**2 + (y-b)**2 - r**2) < d**2:
                img[y,x] = 255

# drawing line
# cv.line(img,(0, 0), (50, 50), (255,255,255), 3)
def Draw_line(x1, y1, x2, y2):

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    
    x = x1
    y = y1
    
    for _ in range(max(dx, dy) + 1):
        img[y, x] = 255
        x += sx
        y += sy

# Circle(150,100,50)
# Circle_border(150,100,50,15)
Draw_line(150,150,200,150)

cv.imshow("Drawing", img)

cv.waitKey(0)

cv.destroyAllWindows()