# -*- coding: utf-8 -*-
"""
Created on Sun May  8 11:27:21 2022

@author: Gustavo
"""

import cv2 
import numpy as np
import math

im=cv2.imread('que.jpg',0)
ims=im.shape
imf=np.zeros((ims[0],ims[1]))

a=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
b=a.transpose()

for x in range(ims[0]):
    for y in range(ims[1]):
        for o in range(0,3):
            for p in range(0,3):
               gx=im[x,y]*a[o,p]
               gy=im[x,y]*b[o,p]
               imf[x,y]=math.sqrt(gx**2+gy**2)

cv2.imshow("Prewitt",imf)
cv2.waitKey(0)
cv2.destroyAllWindows()

a=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
b=a.transpose()

for x in range(ims[0]):
    for y in range(ims[1]):
        for o in range(0,3):
            for p in range(0,3):
               gx=im[x,y]*a[o,p]
               gy=im[x,y]*b[o,p]
               imf[x,y]=math.sqrt(gx**2+gy**2)

cv2.imshow("Sobel",imf)
cv2.waitKey(0)
cv2.destroyAllWindows()

a=np.array([1,4,1])
b=a.transpose()

for x in range(ims[0]):
    for y in range(ims[1]):
        for o in range(0,3):
               gx=im[x,y]*a[o]
               gy=im[x,y]*b[o]
               imf[x,y]=math.sqrt(gx**2+gy**2)

cv2.imshow("Laplaciano",imf)
cv2.waitKey(0)
cv2.destroyAllWindows()