# Entradas 
MENSAJE_BIENVENIDA = 'Muy buenos dias, despierte que esta en clase de 6'
PREGUNTA_MENU = ''' Ingrese 
    1. Para mostrar numeros del 1-5
    2. Para preguntar tu nombre 
    3. Para mostrar el año en el que estamos 
    4.Salir 
'''
PREGUNTA_NOMBRE = 'Ingrese su nombre por favor : '
MENSAJE_ERROR = 'Por favor ingresa una opcion valida'

# Codigo
entrada = 1
while ( entrada >= 1 and entrada <= 3):
    entrada = int (input (PREGUNTA_MENU))
    print (entrada)
    if (entrada == 1):
        print (1,2,3,4,5)
    elif (entrada == 2):
        nombre = input (PREGUNTA_NOMBRE)
        print (f'Bienvenido {nombre} a este menu emplea otras opciones')
    elif (entrada == 3) :
        print ('Estamos en el año 2021')
    elif (entrada == 4):
        print ('Muchas gracias por usar el programa feliz dia')
    else:
        entrada = 1
        print (MENSAJE_ERROR)


