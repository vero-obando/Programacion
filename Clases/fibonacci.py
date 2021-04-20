#numero1 = 0
#numero2 = 1
#numero3 = 1
#numero4 = 2
#numero5 = 3
#numero6 = 5

def sucesionFibonacci (numeroSuc):
    numeroSuc -= 1
    valorMostrar = 0
    numeroActual = 1
    numeroAnterior = 0
    if numeroSuc == 1:
        valorMostrar = 0
    elif numeroSuc == 2:
        valorMostrar = 1
    else:
        print ('Calcular sucesion')
        for i in range(numeroSuc- 1):
            auxiliar = numeroActual
            numeroNuevo = numeroActual + numeroAnterior
            numeroActual = numeroNuevo
            numeroAnterior = auxiliar
        valorMostrar = numeroActual
    return valorMostrar



