# Mensajes
MENSAJE_SAUDAR = 'Bienvenido te apoyare ahorrando'
MENSAJE_AHORRO = 'Llevas ahorrado ...'
PREGUNTAR_VELOR_CPU = 'Cuanto vale el pc que deseas ? :'
PREGUNTA_CUANTO_TIENE = 'Cuanto llevas ahorrado? : '

# Entradas 
print (MENSAJE_SAUDAR)
valor = float (input(PREGUNTAR_VELOR_CPU))
ahorrado = float (input(PREGUNTA_CUANTO_TIENE))

while (valor > ahorrado):
    print (MENSAJE_AHORRO, ahorrado, "Te faltan...", valor - ahorrado)
    ahorrado = ahorrado + 1000 
print (valor == ahorrado)