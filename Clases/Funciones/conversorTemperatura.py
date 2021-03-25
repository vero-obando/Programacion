def conversionTemperatura (temperaturas, unidad):
    ''' Convierte una lista de temperaturas
    segun la unidad ingresada...
    K. Kelvin
    F. Fahreheint
    Devuelve la lista convertida en las unidades deseadas,
    Si se ingresa un valor no valido retorna None
    '''
    listaConvertida = []
    for temperatura in temperaturas:
        conversion = None
        if unidad == 'F':
            conversion = temperatura * 1.8 + 32
        elif unidad == 'K':
            conversion = temperatura + 273.15
        else:
            listaConvertida = None
        listaConvertida.append(conversion)
    return listaConvertida

def clasificarTemperaturas (temperaturas):
    ''' Retorna la clasificacion de las temperaturas ingresadas,
    deben estar del Celsius'''
    listaClasificacion = []
    estado = None 
    for temperatura in temperaturas:
        if temperatura < 36:
            estado = 'Hipotermia'
        elif temperatura >= 36 and temperatura < 37.6:
            estado = 'Normal'
        else:
            estado = 'Fiebre'
        listaClasificacion.append(estado)
    return listaClasificacion

def mostrarTopes (lista):
    mayor = round(max(lista),2)
    menor = round(min(lista),2)
    periodoHoras = round(24/len(lista),2)
    print ('La mayor temperatura es,', mayor)
    print ('La menor temperatura es,', menor)
    print ('El periodo de muestras es,', periodoHoras)
