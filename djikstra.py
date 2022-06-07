# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 23:19:24 2022

@author: Gustavo
"""

import networkx as nx
import random 
import matplotlib.pyplot as plt
import tkinter as tt
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter.ttk import Label

class dij():
    def __init__(self):
        self.pais =""
        self.otro=""
        self.ab=["AFGANISTÁN","GABÓN","SINGAPUR","NAURU", "EL SALVADOR", "ALEMANIA", "NEPAL"]
        self.b=["CAMBOYA", "NAMIBIA","BRUNÉI", "MADAGASCAR", "GEORGIA", "EGIPTO", "GAMBIA" ]
        self.c=["ALBANIA", "GHANA", "MACEDONIA", "MALASIA", "SOMALIA", "ECUADOR", "SIRIA"]
        self.d=["CABO VERDE", "CAMERÚN", "EMIRATOS ÁRABES UNIDOS", "SIERRA LEONE", "BULGARIA", "NICARAGUA", "BRASIL"]
        self.a=[" "]
        self.ve=0
        
    def info(self,y):
        self.pais=y
        
    def info2(self,y):
        self.otro=y
        
    def van(self, ven):
       if self.ve==1:
           ven.destroy()
       von=tt.Tk()
       von.title("Risk: Djikstra version") 
       von.config(bg="grey")
       von.geometry("300x325") 
       image1 = Image.open("world.jpg")
       test = ImageTk.PhotoImage(image1)
       ld = tt.Label(image=test)
       ld.image = test
       ld.place(x=-300,y=-200)
       ba3=ttk.Button(
           von, 
           text="Mapa 1", 
           command=lambda: r.ven(1,von)
           )
       ba3.grid(row=4)
       ba4=ttk.Button(
           von, 
           text="Mapa 2", 
           command=lambda: r.ven(2,von) 
           )
       ba4.grid(row=5)
       ba5=ttk.Button(
           von, 
           text="Mapa 3", 
           command=lambda: r.ven(3,von) 
           )
       ba5.grid(row=6)
       ba6=ttk.Button(
           von, 
           text="Mapa 4", 
           command=lambda: r.ven(4,von) 
           )
       ba6.grid(row=7)
       von.mainloop()
       
    def ven(self, t, von):
       von.destroy()
       
       if t == 1:
            self.a=self.ab
       elif t == 2:
            self.a=self.b
       elif t == 3:
           self.a=self.c
       elif t == 4:
           self.a=self.d
       ven=tt.Tk()
       ven.title("Risk: Djikstra version") 
       ven.config(bg="grey")
       ven.geometry("800x525") 
       image1 = Image.open("world.jpg")
       test = ImageTk.PhotoImage(image1)
       ld = tt.Label(image=test)
       ld.image = test
       ld.place(x=-300,y=-200)
       ba1=ttk.Button(
           ven, 
           text=self.a[0], 
           command=lambda: r.info(self.a[0])
           )
       ba1.grid(row=2)
       ba11=ttk.Button(
           ven, 
           text=self.a[1], 
           command=lambda: r.info(self.a[1])
           )
       ba11.grid(row=3)
       ba3=ttk.Button(
           ven, 
           text=str(self.a[2]), 
           command=lambda: r.info(self.a[2])
           )
       ba3.grid(row=4)
       ba4=ttk.Button(
           ven, 
           text=str(self.a[3]), 
           command=lambda: r.info(self.a[3]) 
           )
       ba4.grid(row=5)
       ba5=ttk.Button(
           ven, 
           text=str(self.a[4]), 
           command=lambda: r.info(self.a[4]) 
           )
       ba5.grid(row=6)
       ba6=ttk.Button(
           ven, 
           text=str(self.a[5]), 
           command=lambda: r.info(self.a[5]) 
           )
       ba6.grid(row=7)
       ba7=ttk.Button(
           ven, 
           text=str(self.a[6]), 
           command=lambda: r.info(self.a[6])
           )
       ba7.grid(row=8)
       b1=ttk.Button(
           ven, 
           text=str(self.a[0]), 
           command=lambda: r.info2(self.a[0])
           )
       b1.grid(row=2, column=2)
       b2=ttk.Button(
           ven, 
           text=str(self.a[1]), 
           command=lambda: r.info2(self.a[1])
           )
       b2.grid(row=3, column=2)
       b3=ttk.Button(
           ven, 
           text=str(self.a[2]), 
           command=lambda: r.info2(self.a[2])
           )
       b3.grid(row=4, column=2)
       b4=ttk.Button(
           ven, 
           text=str(self.a[3]), 
           command=lambda: r.info2(self.a[3])
           )
       b4.grid(row=5, column=2)
       b5=ttk.Button(
           ven, 
           text=str(self.a[4]), 
           command=lambda: r.info2(self.a[4])
           )
       b5.grid(row=6, column=2)
       b6=ttk.Button(
           ven, 
           text=str(self.a[5]), 
           command=lambda: r.info2(self.a[5])
           )
       b6.grid(row=7, column=2)
       b7=ttk.Button(
           ven, 
           text=str(self.a[6]), 
           command=lambda: r.info2(self.a[6])
           )
       b7.grid(row=8, column=2)
       b8=ttk.Button(
           ven, 
           text="Atacar", 
           command=lambda: r.grafo()
           )
       b8.grid(row=9, column=2)
       b9=ttk.Button(
           ven, 
           text="Regresar", 
           command=lambda: r.mapa(ven)
           )
       b9.grid(row=10, column=2)
       ven.mainloop()
      
    def mapa(self,ven):
        self.ve=1
        r.van(ven)

    def grafo(self):
        g =nx.Graph()

        g.add_nodes_from(self.a[:])

        for x in range(14):
            n=random.randint(0,6)
            n1=random.randint(0,6)
            if n==n1 and n!=6:
                n1+1
            elif n==n1:
                n1-2
            g.add_edge(self.a[n],self.a[n1], weight=(3*n+3+n1))

        pos = nx.spring_layout(g, seed=0)

        print(nx.shortest_path(g, self.pais, self.otro))
        r= nx.shortest_path(g, self.pais, self.otro)

        for x in range(len(nx.shortest_path(g, self.pais, self.otro))):
            if (x+1)<len(nx.shortest_path(g, self.pais, self.otro)):
                      nx.draw_networkx_edges(
                          g,
                          pos,
                          edgelist=[(r[x],r[x+1])],
                          width=8,
                          alpha=0.5,
                          edge_color="tab:red")


        nx.draw(g,pos, with_labels=True )
        edge_labels = nx.get_edge_attributes(g, "weight")
        nx.draw_networkx_edge_labels(g, pos, edge_labels)
        plt.show()

r= dij()

r.van(0)   
    






