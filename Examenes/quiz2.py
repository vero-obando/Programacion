# Mensajes
mensaje_bienvenida = 'Bienvenido este es un programa para las temperaturas corporales'
mensaje_salida = 'Que tenga un feliz dia'
mensaje_error = 'Por favor ingrese una opcion valida'
mensaje_punto2 = ' Se muestra primero lista de temperaturas y luego su respectivo estado'
mensaje_temperaturaMax = 'La temperatura maxima es...'
mensaje_temperaturaMin = 'La temperatura minima es...'
pregunta_menu = ''' Ingrese la opcion que desea realizar 
    1. Convertir temperaturas de Celsius a Fahrenheit o a Kelvin 
    2. Estado en el que se encuentra eel paciente segun temperatura
    3. Temperatura maxima Y minima 
    4. Salir
R/:
'''
pregunta_temperaturas = ''' Mostrar temperaturas en :
    C. Celsius.
    F. Fahrenheit
    K. Kelvin
R/:
'''

# Codigo
print (mensaje_bienvenida)
listaCelsius = [36, 37, 38, 35, 36, 38, 37.5, 38.2, 41, 37.4, 38.6, 39.1, 40.3, 33]

listaKelvin = []
for elemento in listaCelsius:
    listaKelvin.append (elemento + 273.15)
listaFahrenheit = []
for elemento in listaCelsius:
    listaFahrenheit.append((elemento*1.8)+32)

listaEstadoTemperaturas = []
for temperatura in listaCelsius :
    estado = ''
    if (temperatura < 36):
        estado = 'Hipotermia'
    elif (temperatura >= 37.6):
        estado = 'Fiebre'
    else:
        estado = 'Normal'
    listaEstadoTemperaturas.append(estado)

opcionElegida = int (input (pregunta_menu))
while (opcionElegida != 4):
    if (opcionElegida == 1):
        opcionTemperatura = input (pregunta_temperaturas)
        if (opcionTemperatura == 'C'):
            print ('Mostrando temperaturas en grados Celsius')
            print (listaCelsius)
        elif (opcionTemperatura == 'F'):
            print ('Mostrando temperaturas en grados Fahrenheit')
            print (listaFahrenheit)
        elif (opcionTemperatura == 'K'):
            print ('Mostrando temperaturas en grados Kelvin')
            print (listaKelvin)
        else:
            print (mensaje_error)
    elif (opcionElegida == 2):
        print (mensaje_punto2)
        print (listaCelsius)
        print (listaEstadoTemperaturas)
    elif (opcionElegida == 3):
        print (mensaje_temperaturaMax, max(listaCelsius))
        print (mensaje_temperaturaMin, min(listaCelsius))
    else:
        print (mensaje_error)
    opcionElegida = int (input (pregunta_menu))

print (mensaje_salida)

