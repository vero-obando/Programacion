# Constantes 
PREGUNTA_PESO = "¿Cuanto pesas? : "
PREGUNTA_ESTATURA = "¿Cuanto mides en metros? : "
MENSAJE_BIENVENIDA = "Hola ¿como estas?, voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "Tu IMC es..."
# Entrada del codigo
print (MENSAJE_BIENVENIDA)
peso = float (input(PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
imc = peso / (estatura**2)
print (MENSAJE_DESPEDIDA, imc)
isObeso = imc >= 30 
print ("el resultado de la prueba obesidad es", isObeso)