# Entradas
MENSAJE_SALUDO = 'Bienvenido a este programa, juguemos'
PREGUNTAR_NUMERO = '''
        En este juego debes asertar un numero
        que va desde el 1-10, la ideas es que
        lo puedes intentar las veces que quieras
        ¡muchos exitos!
        Ingresa tu numero :
'''
PREGUNTA_FALLASTE = 'Ahh fallaste, ingresa otro numero : '
MENSAJE_GANASTE = 'Felicidades ganaste'
MENSAJE_PERDISTE = 'Perdiste, vuelve a intentarlo'

# Codigo 
numeroOculto = 7
vidas = 3
print (MENSAJE_SALUDO)
numeroIngresado = int (input (PREGUNTAR_NUMERO))
if (numeroOculto != numeroIngresado):
    vidas -= 1
while (numeroOculto != numeroIngresado and vidas > 0):
    numeroIngresado = int (input(PREGUNTA_FALLASTE))
    vidas -= 1 

if (vidas > 0):
    print (MENSAJE_GANASTE)
    print (vidas)
else: 
    print (MENSAJE_PERDISTE, ', el numero era...', numeroOculto)
