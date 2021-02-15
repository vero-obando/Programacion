# Datos iniciales
numeroA = 18
numeroB = 22
# Practica de falso y verdadero 
print ("#"*15, "numeroA mayor que numeroB", "#"*15)
isMayorQue = numeroA > numeroB
print (isMayorQue)
print ("#"*15, "numeroB menor que 50", "#"*15)
isMenorQue = numeroB < 50
print (isMenorQue)
print ("#"*15, "numeroA diferente a numeroB", "#"*15)
isDiferenteQue = numeroA != numeroB
print (isDiferenteQue)
print ("#"*15, "numeroA igual a 20", "#"*15)
isIgualQue = numeroA == 20
print (isIgualQue)
# Operaciones basicas
suma = numeroA + numeroB
print ("el resultado de la suma entre el numeroA y numeroB es", suma)
resta = numeroA - numeroB
print ("al restar el numeroA menos el numeroB da como resultado", resta)
multiplicacion = numeroA * 5
print ("si se multiplica al numeroA por cinco, el resultado es", multiplicacion)
division = numeroB / numeroA 
print (f"al dividir al numeroB entre el numeroA da {division} exitosamente")
exponente = numeroB ** 2
print (f"si se eleva al numeroB a la dos da {exponente}")
# Datos extras 
nombreCompleto = "Veronica Obando Builes"
nombre = "Veronica"
apellido1 = "Obando"
apellido2 = "Builes"
# Practica de falso y verdadero 
print ("#"*15, "¿Veronica hace parte del nombre completo?", "#"*15)
isNombreIn = nombre in nombreCompleto
print (isNombreIn)
print ("#"*15, "¿Lopez es uno de los apellidos?", "#"*15)
isApellidoIn = "Lopez" in nombreCompleto
print (isApellidoIn)
print ("#"*15, "Obando NO hace parte de los apellidos", "#"*15)
isApellidoNo = apellido1 not in nombreCompleto
print (isApellidoNo)
print ("#"*15, "¿ Obando Builes son los apellidos?", "#"*15)
isApellidos = apellido1 and apellido2 in nombreCompleto
print (isApellidos)