# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 12:25:14 2022

@author: Gustavo
"""

import cv2 


im=cv2.imread('mm3.jpg',cv2.IMREAD_COLOR)
r,g,b=cv2.split(im)
di=im.shape

for x in range(di[0]):
    for y in range(di[1]):
        q=r[x,y]/(r[x,y]+g[x,y]+b[x,y])
        w=g[x,y]/(r[x,y]+g[x,y]+b[x,y])
        e=b[x,y]/(r[x,y]+g[x,y]+b[x,y])
        if 0.4437>=q>=0.3676 or 0.2948<=w<=0.3235 or 0.2613<=e<=0.3088:
            
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
