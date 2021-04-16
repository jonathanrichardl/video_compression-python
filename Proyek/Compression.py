import numpy as np
import cv2

cap = cv2.VideoCapture('Evening_landing.mp4') #Read the video File
while(cap.isOpened()):
    ret,frame = cap.read() #akan dibaca frame per frame, var frame akan menyimpan nilai pembacaanya 
    cv2.imshow(frame) #Frame ditampilkan jadi gambar
    cv2.waitKey(1000) #sleep 1detik 

#next step : compress variabel frame trus disimpan.
