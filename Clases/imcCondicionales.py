# Constantes 
PREGUNTA_PESO = "¿Cuanto pesas? : "
PREGUNTA_ESTATURA = "¿Cuanto mides en metros? : "
MENSAJE_BIENVENIDA = "Hola ¿como estas?, voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "Tu IMC es..."
MENSAJE_BAJO_PESO = "Estas pero delgado!"
MENSAJE_PESO_NORMAL = "Estas en forma"
MENSAJE_SOBREPESO = "Ten cuidado, estas en sobrepeso"
MENSAJE_OBESO = "Estas obeso, tu salud corre riesgo"
# Entrada del codigo
print (MENSAJE_BIENVENIDA)
peso = float (input(PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
imc = peso / (estatura**2)
isBajoPeso = imc < 18.5
isNormal = imc >= 18.5 and imc < 25
isSobrepeso = imc >= 25 and imc < 30
resultado = ""
if (isBajoPeso):
    resultado = MENSAJE_BAJO_PESO
elif (isNormal):
    resultado = MENSAJE_PESO_NORMAL
elif (isSobrepeso):
    resultado = MENSAJE_SOBREPESO
else:
    resultado = MENSAJE_OBESO
print (MENSAJE_DESPEDIDA, imc)
print (resultado)

