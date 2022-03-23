def colores(color = 'rojo'):
    print('Micolor favorito es el: ' + color)
    
colores('azul')
colores()
colores('verde')




def colores():
    pass




def suma (x,y):
    return x + y

total = suma (10,10)
print(total)

def resta (x,y):
    return x - y

total = resta (10,10)
print(total)

def multiplicacion (x,y):
    return x*y

total = multiplicacion(10,10)
print(total)

def division (x,y):
    return x / y

total = division(10,10)
print(total)

def colores(**kwargs):

       print('Este es el color: ' + kwargs['color1']+ '.')
    
colores(color1 = 'rojo', color2 = 'azul', color3 = 'verde', color4 ='amarillo')