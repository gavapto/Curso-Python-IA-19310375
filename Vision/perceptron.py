# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:32:55 2022

@author: Gustavo
"""

import tkinter as tt
from tkinter import ttk
from tkinter.ttk import Label
import numpy as np

class red():
    def lrn(self, x0, f, g, w0, w1, w2):
        t=0.5
        
        c0=x0*w0
        c1=f[g,0]*w1
        c2=f[g,1]*w2
        s=c0+c1+c2

        if s<t or s==0 or s<0:
            n=0
        else:
            n=1
            
        e=f[g,2]-n
        d=0.1*e
        w0=w0+x0*d
        w1=w1+f[g,0]*d
        w2=w2+f[g,1]*d

        return w0, w1, w2
        
    def x00(self,x0, w0, w1, w2):
        t=0.5
        
        c0=x0*w0
        c1=0*w1
        c2=0*w2
        s=c0+c1+c2

        if s<t:
            n=0
        else:
            n=1
        
        l = Label(ven, text="La respuesta es "+str(n))
        l.grid(row=2, column=3) 
    def x10(self,x0, w0, w1, w2):
        t=0.5
        
        c0=x0*w0
        c1=1*w1
        c2=0*w2
        s=c0+c1+c2

        if s<t:
            n=0
        else:
            n=1
        
        l = Label(ven, text="La respuesta es "+str(n))
        l.grid(row=2, column=3) 
    def x01(self,x0, w0, w1, w2):
        t=0.5
        
        c0=x0*w0
        c1=0*w1
        c2=1*w2
        s=c0+c1+c2

        if s<t:
            n=0
        else:
            n=1
        
        l = Label(ven, text="La respuesta es "+str(n))
        l.grid(row=2, column=3) 
    def x11(self,x0, w0, w1, w2):
        t=0.5
        
        c0=x0*w0
        c1=1*w1
        c2=1*w2
        s=c0+c1+c2

        if s<t:
            n=0
        else:
            n=1
        
        l = Label(ven, text="La respuesta es "+str(n))
        l.grid(row=2, column=3) 
        
x0=1
f=np.array([[0,0,0],[1,0,0],[0,1,0],[1,1,1]])

w0=0
w1=0
w2=0

p=red()

for x in range(0,20):
    for y in range(0,4):
        w0,w1,w2=p.lrn(x0,f,y,w0,w1,w2)

ven=tt.Tk()
ven.title("Perceptron") 
ven.config(bg="red")
ven.geometry("270x100") 

b=ttk.Button(
    ven,
    text="Caso 0 0",
    command=lambda: p.x00(x0, w0, w1, w2)
    ).grid(row=1,column=1)
b1=ttk.Button(
    ven, 
    text="Caso 1 0", 
    command=lambda: p.x10(x0, w0, w1, w2)
    ).grid(row=2,column=1)
b2=ttk.Button(
    ven, 
    text="Caso 0 1", 
    command=lambda: p.x01(x0, w0, w1, w2)
    ).grid(row=1,column=2)
b3=ttk.Button(
    ven, 
    text="Caso 1 1", 
    command=lambda: p.x11(x0, w0, w1, w2)
    ).grid(row=2,column=2)

ven.mainloop()      