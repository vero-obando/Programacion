# Falso o verdadero
pruebaV = True
pruebaF = False
print (pruebaF)
print (pruebaV)
pruebaV = pruebaF
print (pruebaV)
# Datos iniciales 
edad = 18
estatura = 1.55 
peso = 55 
NOMBRE = "Veronica Obando Builes"
print ("#"*15, "Mayor Edad", "#"*15)
isMayorEdad = edad >= 18
print (isMayorEdad)
print ("#"*15, "Bajo La Estatura Promedio", "#"*15)
iaMayorEstatura = estatura < 1.70
# Calculando si el peso es diferente de 55
print (iaMayorEstatura)
print ("#"*15, "Peso diferente 55", "#"*15)
isPesoDiferente = peso != 55
print (isPesoDiferente)
# Vamos a ver si el apellido esta en el nombre completo 
apellido = "Obando"
isApellido = apellido in NOMBRE 
print ("#"*15, "Esta El Apellido En El Nombre", "#"*15)
print (isApellido)


