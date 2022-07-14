# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:16:54 2022

@author: Gustavo
"""

opcion1= { "Entrada": "Pasta",
          "Platillo": "Pollo almendrado",
          "Bebida": "Vino Blanco",
          "Postre": "Volcan de chocolate",
          "Costo": "1299"
    }

opcion2= { "Entrada": "Ensalada",
          "Platillo": "Corte sirloin americano",
          "Bebida": "Vino Tinto",
          "Postre": "Pay de queso y cognac",
          "Costo": "2199"
    }

opcion3= { "Entrada": "Crema de calabaza",
          "Platillo": "Langostino rojo y especias",
          "Bebida": "Vino Blanco",
          "Postre": "Suffle de vainilla",
          "Costo": "1799"
    }

extras= { "Aderezo": "50",
         "Vinagreta": "50",
         "Copa extra": "150",
         "Pure de papa": "45"
         
    }
print()

print("Eliga su menu: \n Opcion 1 : \n"+ str(dict(opcion1))+ "\n Opcion 2: \n" + str(dict(opcion2))+ "\n Opcion 3:" )
print(str(dict(opcion3)))
x=int(input())
print("¿Desea algun extra?" + str(dict(extras)))
y=int(input())      

if x==1:
    print("Eligio: " + str(dict(opcion1)))
    if y==1:
        print("y añadio: Aderezo \n Su total es:" + str(int(opcion1["Costo"])+int(extras["Aderezo"])))
    elif y==2:
        print("y añadio: Vinagreta \n Su total es:" + str(int(opcion1["Costo"])+int(extras["Vinagreta"])))
    elif y==3:
        print("y añadio: Copa extra \n Su total es:" + str(int(opcion1["Costo"])+int(extras["Copa extra"])))
    elif y==4:
        print("y añadio: Pure de papa \n Su total es:" + str(int(opcion1["Costo"])+int(extras["Pure de papa"])))  
elif x==2:
    print("Eligio: " + str(dict(opcion2)))
    if y==1:
        print("y añadio: Aderezo \n Su total es:" + str(int(opcion2["Costo"])+int(extras["Aderezo"])))
    elif y==2:
        print("y añadio: Vinagreta \n Su total es:" + str(int(opcion2["Costo"])+int(extras["Vinagreta"])))
    elif y==3:
        print("y añadio: Copa extra \n Su total es:" + str(int(opcion2["Costo"])+int(extras["Copa extra"])))
    elif y==4:
        print("y añadio: Pure de papa \n Su total es:" + str(int(opcion2["Costo"])+int(extras["Pure de papa"])))  
elif x==3:
    print("Eligio: " + str(dict(opcion3)))
    if y==1:
        print("y añadio: Aderezo \n Su total es:" + str(int(opcion3["Costo"])+int(extras["Aderezo"])))
    elif y==2:
        print("y añadio: Vinagreta \n Su total es:" + str(int(opcion3["Costo"])+int(extras["Vinagreta"])))
    elif y==3:
        print("y añadio: Copa extra \n Su total es:" + str(int(opcion3["Costo"])+int(extras["Copa extra"])))
    elif y==4:
        print("y añadio: Pure de papa \n Su total es:" + str(int(opcion3["Costo"])+int(extras["Pure de papa"])))  
else:
    print("Opcion no valida")
    
  
    