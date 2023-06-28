import numpy as np
import cv2

def Bresenham(image, center, radius):
    x = 0
    y = radius
    d = 3 - 2 * radius

    while x <= y:
        Bresenham_points(image, center, x, y)
        x += 1
        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1

def Bresenham_points(image, center, x, y):
    points = [(x, y), (-x, y), (x, -y), (-x, -y),
              (y, x), (-y, x), (y, -x), (-y, -x)]

    for point in points:
        px = center[0] + point[0]
        py = center[1] + point[1]
        # print("point0 = {} point1 = {}".format(point[0],point[1]))
        # if px >= 0 and px < image.shape[1] and py >= 0 and py < image.shape[0]:
        image[py, px] = 255

image = np.zeros((400, 400), dtype=np.uint8)

center = (200, 200)
radius = 100

Bresenham(image, center, radius)

cv2.imshow('Bresenham Circle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
