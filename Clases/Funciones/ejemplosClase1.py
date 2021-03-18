guardar = print ('Hola')
print (guardar)

guardar = round(14.56789,2)
print (guardar)

def linedesing(cantidad = 15, simbolo = '#'):
    print (simbolo*cantidad)
    return None

linedesing(30, '#')
linedesing(10, '*')
linedesing(100,'.')
linedesing ()

# Muestre la lista
def mostrarLista(listaEntrada = []):
    for elemento in listaEntrada:
        print(elemento)
    return None
lista = [ 123, 321, 43, 54, 67]
lista2 = [23, 67, 98, 76, 22, 896]
linedesing (30,'#')
mostrarLista (lista)
linedesing (30, '#')
mostrarLista (lista2)
# Sumar dos numero
def sumar (a = 0 ,b = 0):
    suma = a + b
    return suma 
linedesing ()
resultado = sumar ()
print (resultado)
print (sumar (12,14))
# Restar dos numero
def restar (a = 0 ,b = 0):
    resta = a - b
    return resta
# Multiplicar dos numero
def multiplicar (a = 0 ,b = 0):
    multiplica = a * b
    return multiplica 
# Dividir dos numero
def dividir (a = 0 ,b = 1):
    dividi= a / b
    return dividi

linedesing ()
print (restar(83,87))
print (multiplicar (83,87))
print (dividir (83,87))

# Exponentes
def potencia (a = 0 ,b = 1):
    exponente = a ** b
    return exponente

print (potencia (2,3))