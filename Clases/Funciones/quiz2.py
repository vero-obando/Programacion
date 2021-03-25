import conversorTemperatura as ct
import funciones as fn 
PREGUNTA_NUMERO = '''Ingrese algun de estas opciones
    1. Conversion temperaturas
    2. Clasificacion temperaturas
    3. Mostrar valor mas alto, mas bajo y periodo
    4. Salir
'''
preguntaTemperatura = ''' 
    C. Celsius
    K. Kelvin
    F. Fahrenheint
'''
mensajeCelsius = 'Mostrando lista original'
mensajeFahrenheint = 'Mostrando lista en fahrenheint'
mensajeKelvin = 'Mostrando lista en kelvin'
mensajeDespedida = 'Que tengas un feliz dia'
mensajeError = 'Valor ingresado no valido'

temperaturaCorporal = [36, 37, 38, 35, 36, 38, 37.5, 38.2, 41, 37.4, 38.6, 39.1, 40.3, 33]

temperaturaCorporalFahrenheint = ct.conversionTemperatura(temperaturaCorporal, 'F')
temperaturaCorporalKelvin = ct.conversionTemperatura(temperaturaCorporal, 'K')
clacificacionTemperaturas = ct.clasificarTemperaturas (temperaturaCorporal)

opcionEscogida = int (input(PREGUNTA_NUMERO))
while (opcionEscogida != 4):
    if (opcionEscogida == 1):
        opcionTemperatura = input (preguntaTemperatura)
        if (opcionTemperatura == 'C' ):
            print (mensajeCelsius)
            fn.mostrarLista(temperaturaCorporal)
        elif (opcionTemperatura == 'F'):
            print (mensajeFahrenheint)
            fn.mostrarLista(temperaturaCorporalFahrenheint)
        elif (opcionTemperatura == 'K'):
            print (mensajeKelvin)
            fn.mostrarLista(temperaturaCorporalKelvin)
        else:
            print (mensajeError)
    elif (opcionEscogida == 2):
        print ('Mostrando clasificacion')
        print ('°C','\t','Clasificacion')
        fn.mostrar2lista(temperaturaCorporal, clacificacionTemperaturas)
    elif (opcionEscogida == 3):
        ct.mostrarTopes(temperaturaCorporal)
    else:
        print (mensajeError)
    opcionEscogida = int (input(PREGUNTA_NUMERO))
print(mensajeDespedida)

