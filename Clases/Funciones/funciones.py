def linedesing(cantidad = 15, simbolo = '#'):
    print (simbolo*cantidad)
    return None
# Sumar dos numero
def sumar (a = 0 ,b = 0):
    '''
    devuelve la suma de dos numeros a y b,
    por defecto a y b valen cero
    '''
    suma = a + b
    return suma 
# Restar dos numero
def restar (a = 0 ,b = 0):
    '''
    devuelve la resta de dos numeros a y b,
    por defecto a y b valen cero
    '''
    resta = a - b
    return resta
# Multiplicar dos numero
def multiplicar (a = 0 ,b = 0):
    '''
    devuelve la multiplicacion de dos numeros a y b,
    por defecto a y b valen cero
    '''
    multiplica = a * b
    return multiplica 
# Dividir dos numero
def dividir (a = 0 ,b = 1):
    '''
    devuelve la division de dos numeros a y b,
    por defecto a es cero y b es uno
    '''
    dividi= a / b
    return dividi
# Exponentes
def potenciar (a = 0 ,b = 1):
    '''
    devuelve la potenciacion de dos numeros a y b,
    por defecto a (base) es cero y b (exponente) es uno
    '''
    potencia = a ** b
    return potencia
# Funciones dependientes de otras
def calcular (operacion, numeroA, numeroB):
    '''
    devuelve el calculo de dos numeros a y b,
    respecto a la operacion que se de
    '''
    print (operacion(numeroA, numeroB))

def mostrarLista (lista):
    for elemento in lista:
        print (elemento)

def mostrar2lista (lista1, lista2):
    for i in range (len(lista1)):
        print (lista1[i], '\t', lista2[i])
