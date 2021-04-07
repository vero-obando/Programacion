# Ejercicios funciones 
# Mostrar lista elemento por elemento 
def mostrarLista (lista):
    '''
    Muestra lista elemento a elemento
    '''
    for elemento in lista:
        print (elemento)
# Numero mas grande, mas pequeño y promedio de la lista 
def mostrarDatosGenerales (lista):
    '''
    Muestra el numero mayor, el menor y el promedio de una lista
    '''
    mayor = round(max(lista),2)
    menor = round(min(lista),2)
    promedio = round (sum(lista)/len(lista),2)
    print ('El mayor numero de la lista es...', mayor)
    print ('El menor numero de la lista es...', menor)
    print ('El promedio de la lista es...', promedio)
# Saludar n veces 
def saludo (veces = 1, saludo = 'Hola '):
    '''
    Poner primero el numero por cuantes veces se saludara 
    y luego el saludo que se desea dar.
    Por defecto las veces es 1 y el saludo es Hola.
    '''
    print (veces*saludo)
    return None
# Devolver numeros pares 
def numerosPares (lista):
    '''
    Devuelve solo numeros pares de una lista 
    '''
    pares = []
    for iteracion in lista:
        if (iteracion%2 == 0):
            pares.append(iteracion)
    return pares

listaEjem = [1,2,3,4,5,6,7,8,9]
listaPares = numerosPares(listaEjem)
print (listaPares)
# Devolver los numeros mayores de 24
def MayorA24 (lista):
    '''
    Devuelve numeros de la lista mayores a 24
    '''
    Mayores24 = []
    for elemento in lista:
        if(elemento > 24):
            Mayores24.append(elemento)
    return Mayores24

lista2 = [20,21,26,67,90,1,3,76]
listaMayores24 = MayorA24 (lista2)
print (listaMayores24)
# Calcular IMC
def calcularIMC (peso, altura):
    '''
    Calcula el IMC poniendo primero el peso y luego la altura
    '''
    IMC = peso/(altura**2) 
    return IMC

ejemIMC = calcularIMC(50,1.50)
print('Tu IMC es de ',ejemIMC)
# Despedirse del que ejecuta el codigo
def despedirse ():
    '''
    Mensaje de despedida
    '''
    print ('Adios, que tengas un feliz dia')

despedirse()
