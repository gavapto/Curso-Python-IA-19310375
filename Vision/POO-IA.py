# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 19:27:22 2022

@author: Gustavo
"""
import scanf

class datos ():
   
    def suma(self, d1, d2):
        re=d1+d2
        print("El resultado de la suma es ", re)
        pass
    
    def resta (self,d1,d2):
        re=d1-d2
        print("El resultado  de la resta es ", re)
        pass
    
    def multi(self,d1,d2):
        re=d1*d2
        print("El resultado de la multiplicacion es ", re)
        pass
    
    def div (self,d1,d2):
        if(d2==0):
           print("El resultado de la division es indefinido") 
        else:
            re=d1/d2
            print("El resultado de la division es ", re)
        pass
    
a=datos()

d1=27
d2=11

a.suma(d1, d2)    
a.resta(d1, d2)
a.multi(d1, d2)
a.div(d1, d2)

d3=scanf.scanf("%d")