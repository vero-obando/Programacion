PREGUNTA_NUMERO = '''Ingrese algun de estas opciones
    1. Hacer conversion de pesos a dolares o euros 
    2. Agregue un valor a la lista de pesos
    3. Mostrar valor mas alto, mas bajo y promedio
    4. Puedes eliminar algun elemento de la lista
    5. Salir
'''
preguntaMoneda = ''' 
    C. Mostrar en pesos colombianos
    D. Mostrar en dolares
    E. Mostrar en euros
'''
preguntarNumero= 'Ingrese un valor en COP : '
mensajeMayor = 'El mayor numero ingresado es...'
mensajeMenor = 'El menor numero ingresado es...'
mensajePromedio = 'El promedio es ...'
mensajeBorrarCoordenada = 'Ingrese la posicion que desea borrar : '

listaPesos = [20000, 30000, 4000, 2500, 1000, 7600]
# Conversor punto 1 
listaEuros = []
for elemento in listaPesos:
    conversor = round (elemento*0.00023, 2)
    listaEuros.append(conversor)
listaDolares = []
for elemento in listaPesos:
    conversor = round (elemento*0.00028, 2)
    listaDolares.append(conversor)

opcionElegida = int(input(PREGUNTA_NUMERO))
while (opcionElegida != 5):
    is1 = opcionElegida == 1
    is2 = opcionElegida == 2
    is3 = opcionElegida == 3
    is4 = opcionElegida == 4
    isnotvalid = opcionElegida != 5
    # punto 1
    if(is1):
        opcionMoneda= input (preguntaMoneda)
        if (opcionMoneda == 'C' ):
            print ('Mostrando lista original')
            print (listaPesos)
        elif (opcionMoneda == 'D'):
            print ('Mostrando lista en dolares')
            print (listaDolares)
        elif (opcionMoneda == 'E'):
            print ('Mostrando lista en euros')
            print (listaEuros)
        else:
            print ('valor ingresado no valido')
    #punto 2
    elif (is2):
        valorIngresado = float (input (preguntarNumero))
        listaPesos.append (valorIngresado)
        print (listaPesos)
    # punto 3
    elif (is3):
        print (mensajeMayor, max(listaPesos))
        print (mensajeMenor, min(listaPesos))
        print (mensajePromedio, sum(listaPesos)/len(listaPesos))
    # punto 4
    elif (is4):
        print (listaPesos)
        posicion = int (input(mensajeBorrarCoordenada)) -1
        listaPesos.pop(posicion)
        print (listaPesos)
    # opcion no valida
    else:
        print ('respuesta no valida')
    opcionElegida = int(input(PREGUNTA_NUMERO))

print('feliz dia')

