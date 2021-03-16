# Mensajes
mensaje_bienvenida = 'Bienvenido, espero se encuentre muy bien'
mensaje_salida = 'Que tenga un feliz dia'
mensaje_error = 'opcion NO valida'
mensajeMayor = 'El ingreso mas alto es ...'
mensajeMenor = 'El ingreso menor es ...'
mensajePromedio = 'El promedio de los ingresos es...'
pregunta_numero = ''' Ingrese la opcion que desea realizar
    1.  Conversion de dolares a pesos colombianos o euros 
    2. Clasificacion de ingresos mensuales en dolares
    3. Ingero mas alto, mas bajo y el promedio
    4. Salir.
R/:
'''
pregunta_moneda = ''' Mostrar lista en...
    C. Pesos colombianos
    D. Dolares
    E. Euros
R/:
'''

# Codigo
print (mensaje_bienvenida)
listaDolares = [20000, 30000, 4000, 2500, 1000, 7600]
# Punto 1
listaPesos = []
for elemento in listaDolares:
    listaPesos.append (elemento * 3700)
listaEuros = []
for elemento in listaDolares:
    listaEuros.append(elemento * 0.84)
# Punto 2
listaClasificacion = []
for ingreso in listaDolares :
    clasificacion = ''
    if (ingreso < 1000):
        clasificacion = 'Ingresos mensuales bajos'
    elif (1000 < ingreso < 7000):
        clasificacion = 'ingresos mensuales medios'
    elif (7000 < ingreso < 20000):
        clasificacion = 'ingresos mensuales altos'
    else:
        clasificacion = 'ingresos mensuales elevados'
    listaClasificacion.append (clasificacion)

opcionElegida = int (input(pregunta_numero))
while (opcionElegida != 5):
    if (opcionElegida == 1):
        opcionMoneda = input (pregunta_moneda)
        if (opcionMoneda == 'C'):
            print ('Mostrando lista en pesos Colombianos')
            print (listaPesos)
        elif (opcionMoneda == 'D'):
            print ('Mostrando lista en Dolares')
            print (listaDolares)
        elif (opcionMoneda == 'E'):
            print ('Mostrando lista en Euros')
            print (listaEuros)
        else:
            print (mensaje_error)
    elif (opcionElegida == 2):
        print (listaDolares)
        print(listaClasificacion)
    elif (opcionElegida == 3):
        print (mensajeMayor, max(listaDolares))
        print (mensajeMenor, min(listaDolares))
        print (mensajePromedio, sum(listaDolares)/len(listaDolares))
    elif (opcionElegida == 4):
        print (mensaje_salida)
    else :
        print (mensaje_error)
    opcionElegida = int (input(pregunta_numero))

print (mensaje_salida)
