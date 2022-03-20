# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:12:09 2022

@author: Gustavo
"""

a = [1,2,3,4,5,6,7,8,9,10]

for x in range(len(a)):
    print(a[x])
    for y in "cebolla":
        a[x]+= 2
else:
    print(a)

for x in range(2,40,3):
    print("Tengo mucha hambre")
    if x == 29:
        print("ahora si, a comer")
        break
    else:
        print("Pero primero hay que terminar")
        print(x)
    