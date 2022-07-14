# -*- coding: utf-8 -*-
"""
Created on Wed May 11 13:15:22 2022

@author: Gustavo
"""

import cv2 
import numpy as np

im=cv2.imread('sal.jpg',0)
ims=im.shape
imf=np.zeros((ims[0],ims[1]))
            
imf = cv2.blur(im,(3,3))

imf2= cv2.GaussianBlur(im,(5,5),1)
 
cv2.imshow("Original",im)
cv2.waitKey(0)
cv2.destroyAllWindows()
       
cv2.imshow("Filtro lineal: media",imf)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Filtro lineal: Gaussiano",imf2)
cv2.waitKey(0)
cv2.destroyAllWindows()
