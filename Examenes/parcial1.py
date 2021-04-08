# Parcial funciones
def mostrarCalculos (a ,b ,c ):
    '''
    Dados 3 numeros se muestra en pantalla la suma, la resta,
    la multiplicacion, la division y la potencia entre ellos.
    '''
    suma = a + b + c
    resta = a - b - c
    multiplicacion = a*b*c
    division = a/b/c
    potenciacion = a**b**c
    print('La suma es ', suma)
    print ('La resta es', resta)
    print ('La multiplicacion es ', multiplicacion)
    print ('La division es ', division)
    print ('La potencia es ', potenciacion)
    return None

mostrarCalculos (4,2,1)

def mostrarListasMismoTamaño (lista1 , lista2, lista3):
    '''
    Muestra en pantalla 3 listas del mismo tamaño
    '''
    if (len (lista1) == len(lista2) == len (lista3)):
        print (lista1, lista2, lista3)
    else:
        print ('Las listas no son del mismo tamaño')
    return None

listaA = [1,2,3,4]
listaB = [5,6,7,8]
listaC = [1,4,6,9]
mostrarListasMismoTamaño(listaA, listaB, listaC)

def areaTriangulo (base, altura):
    '''
    Calcula el area de un triangulo
    '''
    area = ((base*altura)/2)
    return area

baseIngresada = float (input('Ingrese una base : '))
alturaIngresada = float (input('ingrese la altura : '))
area1 = areaTriangulo(baseIngresada, alturaIngresada)
print ('El area del triangulo es ', area1)

def mostrarDatosGenerales (lista):
    '''
    Muestra el numero mayor, el menor y el promedio de una lista de numeros enteros
    '''
    mayor = (max(lista))
    menor = (min(lista))
    promedio = (sum(lista)/len(lista))
    print ('El mayor numero de la lista es...', mayor)
    print ('El menor numero de la lista es...', menor)
    print ('El promedio de la lista es...', promedio)
    return None


