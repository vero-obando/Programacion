
import random
# Entradas
MENSAJE_SALUDO = 'Bienvenido a este programa, juguemos'
MENSAJE_SEGUNDO_NIVEL = 'Felicidades, pasaste el primer nivel, ahora vas por el segundo'
PREGUNTAR_NUMERO = '''
        En este juego debes asertar un numero
        que va desde el 1-10, la ideas es que
        lo puedes intentar antes de que se te acaben 
        las vidas, no hay vida cero
        ¡muchos exitos!
        Ingresa tu numero :
'''
PREGUNTA_DIFICULTAD = '''
    1. Facil
    2. Moderado
    3. Dificil 
    Ingresa tu dificultad :
'''
PREGUNTA_FALLASTE = 'Ahh fallaste, ingresa otro numero : '
MENSAJE_GANASTE = 'Felicidades ganaste'
MENSAJE_PERDISTE = 'Perdiste, vuelve a intentarlo'

# Codigo 
numeroOculto = random.randint(1,10)
numeroOcultoDos = random.randint(1,10)
vidas = None

dificultad = int (input (PREGUNTA_DIFICULTAD))
while (dificultad != 1 and dificultad != 2 and dificultad != 3 ):
    print ('Ingresa una opcion valida')
    dificultad = int (input (PREGUNTA_DIFICULTAD))

if (dificultad == 1):
    print ('Modo facil activado')
    vidas = 10
elif (dificultad == 2):
    print ('Modo moderado activado')
    vidas = 5
else :
    print ('Modo dificil activado')
    vidas = 2

numeroIngresado = int (input(PREGUNTAR_NUMERO))
while (numeroIngresado != numeroOculto and vidas > 1 ):
    if(numeroIngresado > numeroOculto):
        print ('estas caliente ')
    else :
        print ('estas frio')
    vidas -= 1
    print (f'te quedan {vidas} vidas')
    numeroIngresado = int (input(PREGUNTA_FALLASTE))

if (vidas >=0 and numeroIngresado == numeroOculto):
    print (MENSAJE_SEGUNDO_NIVEL)
    numeroIngresado = int (input(PREGUNTAR_NUMERO))
    while (numeroIngresado != numeroOcultoDos and vidas > 1 ):
        if (numeroIngresado > numeroOcultoDos):
            print ('estas caliente')
        else:
            print ('estas frio')
        vidas -= 1
        print (f'te quedan {vidas} vidas')
        numeroIngresado = int (input(PREGUNTA_FALLASTE))

if (vidas >= 0 and numeroIngresado == numeroOcultoDos):
    print (MENSAJE_GANASTE)
else:
    print (MENSAJE_PERDISTE, 'el numero uno era el...', numeroOculto, 'el numero dos era el...', numeroOcultoDos)

