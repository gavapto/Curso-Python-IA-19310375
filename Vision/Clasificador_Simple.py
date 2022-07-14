# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 16:18:45 2022

@author: Gustavo
"""
import cv2 


im=cv2.imread('mm.jpg',cv2.IMREAD_COLOR)
r,g,b=cv2.split(im)
di=im.shape

for x in range(di[0]):
    for y in range(di[1]):
        if 146>=r[x,y]<=225 or 97>=g[x,y]<=198 or 86>=b[x,y]<=189  : 
            r[x,y]=236
            g[x,y]=236
            b[x,y]=236
        else:
             r[x,y]=1
             g[x,y]=1
             b[x,y]=1
        
        

im2=cv2.merge([r,g,b])
cv2.imshow("Manos",im)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Manos b/c",im2)
cv2.waitKey(0)
cv2.destroyAllWindows()
