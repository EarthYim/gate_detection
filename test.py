import cv2
import numpy as np 

cap = cv2.VideoCapture('./image/robosub_01.mp4')

def nothing(x):
    pass

#NOT WROKING
cv2.namedWindow('trackbar')
cv2.createTrackbar('Hmin', 'trackbar', 0, 179, nothing)
cv2.createTrackbar('Smin', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('Vmin', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('Hmax', 'trackbar', 0, 179, nothing)
cv2.createTrackbar('Smax', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('Vmax', 'trackbar', 0, 255, nothing)

while True:

    ret, img = cap.read()
    img = cv2.resize(img, (968, 608))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos('Hmin', 'trackbar')
    s_min = cv2.getTrackbarPos('Smin', 'trackbar')
    v_min = cv2.getTrackbarPos('Vmin', 'trackbar')
    h_max = cv2.getTrackbarPos('Hmax', 'trackbar')
    s_max = cv2.getTrackbarPos('Smax', 'trackbar')
    v_max = cv2.getTrackbarPos('Vmax', 'trackbar')

    lower_a = np.array([0, 0, 0], dtype= 'uint8')
    upper_a = np.array([15, 240, 240], dtype= 'uint8')

    kernel = np.ones((2,2),np.uint8)
    
    mask = cv2.inRange(hsv, lower_a, upper_a)
    mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE, kernel)
    #mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    #mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    res = cv2.bitwise_and(img, img, mask=mask)
    
    #detected parts will be shown in this window
    cv2.imshow('processed', res)
    cv2.imshow('original', img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
