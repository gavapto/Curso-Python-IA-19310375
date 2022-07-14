# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:36:48 2022

@author: Gustavo
"""

import cv2 
import numpy as np

im=cv2.imread('sal.jpg',0)
ims=im.shape
imf=np.zeros((ims[0],ims[1]))
            
a=cv2.getStructuringElement(1,(3,3))
imf=cv2.dilate(im,a)

imf2= cv2.medianBlur(im,3)
 
cv2.imshow("Original",im)
cv2.waitKey(0)
cv2.destroyAllWindows()
       
cv2.imshow("Filtro lineal: Maximo",imf)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Filtro lineal: Mediana",imf2)
cv2.waitKey(0)
cv2.destroyAllWindows()


               