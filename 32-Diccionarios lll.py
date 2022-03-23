teclados ={
"teclado1":  {
    'Categoría':'Teclados',
    'Modelo':'HyoerX Alloy PPS Pro',
    'Precio': '89.99',
    'ID' : '001'
     },

"teclado2":  {
    'Categoría':'Teclados',
    'Modelo':'Corsair K55 RGB',
    'Precio': '59.99'
     }


 }

print(len(teclados))

teclado1=teclados()
teclado2=teclados()
teclado3=teclados()

if 'ID' in teclado2:
    print('El producto tiene un ID especificado')
else:
    print('El producto no tiene un ID especificado,introduce un ID ')


teclado1.update({'Color' : 'Negro'})
print(teclado1)


vistaTeclado = teclado1.keys()
print(vistaTeclado)


teclado3 = dict.fromkeys(teclado3,'vacío')
print(teclado3)


teclado3 = dict(Categoría = 'Teclados',
           Modelo = 'Razer Cynosa Chroma',
            Precio = '49.99' )
print(teclado3)


tecladoCopia = dict(teclado1)
print(tecladoCopia)


teclaCopia = teclado1.copy()
print(teclaCopia)


teclado1['Color'] = 'negro'
print(teclado1)

teclado1.clear()
print(teclado1)


del teclado1
print(teclado1)


del teclado1['Precio']
print(teclado1)


teclado1.pop('Categoría')
print(teclado1)

print(len(teclado1)+ len(teclado2))