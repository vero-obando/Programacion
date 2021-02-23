# Datos
MENSAJE_BIENVENIDA = "Hola, en este programa vamos a clasificar el estado de triglicéridos y homocisteína"
PREGUNTA_TRIGLICERIDOS = "Por favor ingrese el nivel de triglicéridos : "
PREGUNTA_HOMOCISTEINA = "Ahora ingresa el nivel de homocisteína : "
RESULTADO_TRIGLICERIDOS_OPTIMO = "El paciente se encuentra en un estado OPTIMO de triglicéridos"
RESULTADO_TRIGLICERIDOS_SOBRE = "El paciente se encuentra en un estado SOBRE EL LIMITE OPTIMO de triglicéridos"
RESULTADO_TRIGLICERIDOS_ALTO = "El paciente se encuentra en un estado ALTO de triglicéridos"
RESULTADO_TRIGLICERIDOS_MUY = "El paciente se encuentra en un estado MUY ALTO de triglicéridos"
RESULTADO_HOMOCISTEINA_OPTIMO = "El paciente se encuentra en un estado OPTIMO de homocisteína"
RESULTADO_HOMOCISTEINA_SOBRE = "El paciente se encuentra en un estado SOBRE EL LIMITE OPTIMO de homocisteína"
RESULTADO_HOMOCISTEINA_ALTO = "El paciente se encuentra en un estado ALTO de homocisteína"
RESULTADO_HOMOCISTEINA_MUY = "El paciente se encuentra en un estado MUY ALTO de homocisteína"
MENSAJE_DESPEDIDA = "Gracias por utilizar este programa, buen día"

# Codigo
print(MENSAJE_BIENVENIDA)
trigliceridos = int(input(PREGUNTA_TRIGLICERIDOS))
isTrigliceridosOptimo = trigliceridos < 150
isTrigliceridosSobre = 150 <= trigliceridos <= 199
isTrigliceridosAlto = 200 <= trigliceridos <= 499
resultado = ""
if(isTrigliceridosOptimo):
    resultado = RESULTADO_TRIGLICERIDOS_OPTIMO
elif(isTrigliceridosSobre):
    resultado = RESULTADO_TRIGLICERIDOS_SOBRE
elif(isTrigliceridosAlto):
    resultado = RESULTADO_TRIGLICERIDOS_ALTO
else:
    resultado = RESULTADO_TRIGLICERIDOS_MUY
print (resultado)
homocisteina = int(input(PREGUNTA_HOMOCISTEINA))
isHomocisteinaOptimo = 2 <= homocisteina < 15
isHomocisteinaSobre = 15 <= homocisteina < 30
isHomocisteinaAlto = 30 <= homocisteina < 100
respuesta = ""
if(isHomocisteinaOptimo):
    respuesta = RESULTADO_HOMOCISTEINA_OPTIMO
elif(isHomocisteinaSobre):
    respuesta = RESULTADO_HOMOCISTEINA_SOBRE
elif(isHomocisteinaAlto):
    respuesta = RESULTADO_HOMOCISTEINA_ALTO
else:
    respuesta = RESULTADO_HOMOCISTEINA_MUY
print(respuesta)
print(MENSAJE_DESPEDIDA)
