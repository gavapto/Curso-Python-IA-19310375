
# -*- coding: utf-8 -*-

import cv2 

im=cv2.imread('manos.jpg',cv2.IMREAD_COLOR)
cv2.imshow('manos ver',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

vid = cv2.VideoCapture('Video.mp4')
while (True): 
 ret, imagen = vid.read() 
 if (ret == True):
     cv2.imshow('Mostrar video', imagen) 
 if cv2.waitKey(1) & 0xFF == ord('q'): 
     break
vid.release() 
cv2.destroyAllWindows() 

