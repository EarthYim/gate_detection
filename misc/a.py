import cv2
import numpy as np 

cap = cv2.VideoCapture('robosub_01.mp4')

while True:
    ret, img = cap.read()
    print(img.shape)