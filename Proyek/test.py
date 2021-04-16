import numpy as np
import cv2

cap = cv2.VideoCapture('Evening_landing.mp4')
while(cap.isOpened()):
    ret,frame = cap.read()
    print(frame)
    cv2.imshow(frame)
    cv2.waitKey(1000)