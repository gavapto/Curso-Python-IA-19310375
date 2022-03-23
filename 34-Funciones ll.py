def alumnos_profesores(profesor, sustituto, *args):
    print('Profesor: ' + profesor)
    print('Sutituto: ' + sustituto)
    for x in args:
        print('Alumno: ' + x)
        
lista_alumnos = ['Andrés','Ana','Alejandro','Andrea']

alumnos_profesores('Antonio','Amador', *lista_alumnos)