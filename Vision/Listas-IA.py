# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 20:32:16 2022

@author: Gustavo
"""

elec=["arriba","abajo","fondo","cima"]

print(elec)

a=elec.pop(3)
print(elec)

del elec[2]
print(elec)

elec.append("fondo")
print(elec)

elec.insert(3,"cima")
elec.insert(4,"extraño")
print(elec)

elec.remove("extraño")
print(elec)

print(sorted(elec))

print(len(elec))

