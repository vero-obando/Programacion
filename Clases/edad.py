# Entradas 
MENSAJE_BIENVENIDA = "Bienvenido al codigo"
MENSAJE_MAYOR_EDAD = "Eres mayor de edad, puedes seguir"
MENSAJE_MENOR_EDAD = "Eres menor de edad, no puedes seguir"
PREGUNTA_EDAD = "Cuantos años tienes : "
# Codigos 
print (MENSAJE_BIENVENIDA)
edad = int (input(PREGUNTA_EDAD))
isMayor = edad >= 18 
resultado = ""
if (isMayor):
    print (MENSAJE_MAYOR_EDAD)
else:
    print (MENSAJE_MENOR_EDAD)

print (resultado)
