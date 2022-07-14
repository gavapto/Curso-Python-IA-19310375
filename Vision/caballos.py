# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:18:37 2022

@author: Gustavo
"""
import tkinter as tt
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter.ttk import Label
import random 
import pygame


class cab():
    
    def muestra(self,a1,d,an,o,c1,c):
        for x in range(0,25):
            if a1[x]==d:
                s=x+1
                
        pygame.mixer.init()
        sound = pygame.mixer.Sound("caba.mp3")
        sound.play()
        l = Label(ven, text="Caballo numero "+str(s))
        l.grid(row=2, column=6)
        la = Label(ven, text="Nombre del caballo:"+an)
        la.grid(row=4, column=6)
        lc = Label(ven, text="Puesto: "+ str(o))
        lc.grid(row=6, column=6)
        lb = Label(ven, text="Velocidad:"+ str(d))
        lb.grid(row=8, column=6) 
        image1 = Image.open(str(c[c1[s-1]]))
        test = ImageTk.PhotoImage(image1)
        ld = tt.Label(image=test)
        ld.image = test
        ld.place(x=100,y=200)
        b=ttk.Button(
            ven, 
            text="Limpiar", 
            command=lambda: r.olvida(l,la,lb,lc,ld,b)
            ).place(x=100, y=450)
    
    def olvida (self,l,la,lb,lc,ld,b):
        l.grid_forget()
        la.grid_forget()
        lb.grid_forget()
        lc.grid_forget()
        ld.place_forget()
            
    def gana(self,a2,v,a3,ag):
        for x in range(0,5):
            if a2[x]==v[4]:
                if x == 4:
                    a3[0]=v[2]
                    a3[1]=v[3]
                    ag[18]=v[1]
                    ag[17]=v[0]
                if x == 3:
                    a3[2]=v[3]
                    a3[3]=v[4]
                    ag[14]=v[2]
                    ag[15]=v[1]
                    ag[16]=v[0]
                if x == 2:
                    a3[4]=v[4]
                    ag[10]=v[3]
                    ag[11]=v[2]
                    ag[12]=v[1]
                    ag[13]=v[0]
                if x == 0:
                    for x in range(0,5):
                        ag[x]=v[x]
                if x == 1:
                    for x in range(0,5):
                        ag[5+x]=v[x]
        return a3,ag


r=cab()

a= []
a1= []
an=[]
ag=[]
n1=["El Gran ","La Preciosa ","El Rapido ","El Pequeño ","El Colosal "]
n2=["Copo ","Terron ","Gallito ","Amanecer ","Galleta "]
n3=["de azucar","de nieve","de Mayo","de chocolate","de corral"]
c=["caballo1.jpg","caballo2.jpg","caballo3.jpg","caballo4.jpg","caballo5.jpg"]
c1=[]
a2= []
a3= [0,0,0,0,0]
v= []
e= []
l= []
l1= []
z= []

for x in range(0,25):
    a.append(x)
    a1.append(x)
    c1.append(x)
    p=random.randint(0,4)
    o=random.randint(0,4)
    i=random.randint(0,4)
    b=random.randint(0,100)
    j=random.randint(0,4)
    a[x]=b
    a1[x]=b
    c1[x]=j
    an.append(n1[p]+n2[o]+n3[i])
    

for x in range(0,5):
	v.append(a[x])
	e.append(a[x+4])
	l.append(a[x+9])
	l1.append(a[x+19])
	z.append(a[x+19])

v.sort()
e.sort()
l.sort()
l1.sort()
z.sort()

a2.append(v[4])
a2.append(e[4])
a2.append(l[4])
a2.append(l1[4])
a2.append(z[4])
a2.sort()

for x in range(0,19): 
    ag.append(0)
a3,ag=r.gana(a2,v,a3,ag)
a3,ag=r.gana(a2,e,a3,ag)
a3,ag=r.gana(a2,l,a3,ag)
a3,ag=r.gana(a2,l1,a3,ag)
a3,ag=r.gana(a2,z,a3,ag)
a3.sort()
ag.sort()

a[24]=a2[4]
for x in range(0,19):
    a[x]=ag[x]
for x in range(0,5):
    a[19+x]=a3[x]
        
ven=tt.Tk()
ven.title("Carrera de caballos") 
ven.config(bg="brown")
ven.geometry("500x625") 

b=ttk.Button(
    ven,
    text="1° Caballo",
    command=lambda: r.muestra(a1,a[24],an[24],1,c1,c)
    ).grid(row=1)
b1=ttk.Button(
    ven, 
    text="2° Caballo", 
    command=lambda: r.muestra(a1,a[23],an[23],2,c1,c)
    ).grid(row=2)
b2=ttk.Button(
    ven, 
    text="3° Caballo", 
    command=lambda: r.muestra(a1,a[22],an[22],3,c1,c)
    ).grid(row=3)
b3=ttk.Button(
    ven, 
    text="4° Caballo", 
    command=lambda: r.muestra(a1,a[21],an[21],4,c1,c)
    ).grid(row=4)
b4=ttk.Button(
    ven, 
    text="5° Caballo", 
    command=lambda: r.muestra(a1,a[20],an[20],5,c1,c)
    ).grid(row=5)
b5=ttk.Button(
    ven, 
    text="6° Caballo", 
    command=lambda: r.muestra(a1,a[19],an[19],6,c1,c)
    ).grid(row=6)
b6=ttk.Button(
    ven, 
    text="7° Caballo", 
    command=lambda: r.muestra(a1,a[18],an[18],7,c1,c)
    ).grid(row=7)
b7=ttk.Button(
    ven, 
    text="8° Caballo", 
    command=lambda: r.muestra(a1,a[17],an[17],8,c1,c)
    ).grid(row=8)
b8=ttk.Button(
    ven, 
    text="9° Caballo", 
    command=lambda: r.muestra(a1,a[16],an[16],9,c1,c)
    ).grid(row=9)
b9=ttk.Button(
    ven, 
    text="10° Caballo", 
    command=lambda: r.muestra(a1,a[15],an[15],10,c1,c)
    ).grid(row=10)
b01=ttk.Button(
    ven, 
    text="11° Caballo", 
    command=lambda: r.muestra(a1,a[14],an[14],11,c1,c)
    ).grid(row=11)
b02=ttk.Button(
    ven, 
    text="12° Caballo", 
    command=lambda: r.muestra(a1,a[13],an[13],12,c1,c)
    ).grid(row=12)
b03=ttk.Button(
    ven, 
    text="13° Caballo", 
    command=lambda: r.muestra(a1,a[12],an[12],13,c1,c)
    ).grid(row=13)
b04=ttk.Button(
    ven, 
    text="14° Caballo", 
    command=lambda: r.muestra(a1,a[11],an[11],14,c1,c)
    ).grid(row=14)
b05=ttk.Button(
    ven, 
    text="15° Caballo", 
    command=lambda: r.muestra(a1,a[10],an[10],15,c1,c)
    ).grid(row=15)
b06=ttk.Button(
    ven, 
    text="16° Caballo", 
    command=lambda: r.muestra(a1,a[9],an[9],16,c1,c)
    ).grid(row=16)
b07=ttk.Button(
    ven, 
    text="17° Caballo", 
    command=lambda: r.muestra(a1,a[8],an[8],17,c1,c)
    ).grid(row=17)
b07=ttk.Button(
    ven, 
    text="18° Caballo", 
    command=lambda: r.muestra(a1,a[7],an[7],18,c1,c)
    ).grid(row=18)
b08=ttk.Button(
    ven, 
    text="19° Caballo", 
    command=lambda: r.muestra(a1,a[6],an[6],19,c1,c)
    ).grid(row=19)
b09=ttk.Button(
    ven, 
    text="20° Caballo", 
    command=lambda: r.muestra(a1,a[5],an[5],20,c1,c)
    ).grid(row=20)
b11=ttk.Button(
    ven, 
    text="21° Caballo", 
    command=lambda: r.muestra(a1,a[4],an[4],21,c1,c)
    ).grid(row=21)
b12=ttk.Button(
    ven, 
    text="22° Caballo", 
    command=lambda: r.muestra(a1,a[3],an[3],22,c1,c)
    ).grid(row=22)
b13=ttk.Button(
    ven, 
    text="23° Caballo", 
    command=lambda: r.muestra(a1,a[2],an[2],23,c1,c)
    ).grid(row=23)
b14=ttk.Button(
    ven, 
    text="24° Caballo", 
    command=lambda: r.muestra(a1,a[1],an[1],24,c1,c)
    ).grid(row=24)
b15=ttk.Button(
    ven, 
    text="25° Caballo", 
    command=lambda: r.muestra(a1,a[0],an[0],25,c1,c)
    ).grid(row=25)
    
ven.mainloop()
