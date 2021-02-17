# Constantes 
MENSAJE_BIENVENIDA = "Bienvenido, vamos a realizar unas operaciones"
MENSAJE_NUMEROA = "Por favor ingresa un numero, el cual llamaremos numero A : "
MENSAJE_NUMEROB = "Ahora ingresa otro, el cual llamaremos numero B : "
MENSAJE_OPCIONES = "Por favor escoge la operacion que deseas realizar"
listaOpciones = """ 1.Suma 
 2.Resta (A-B)
 3.Resta (B-A)
 4.Multiplicacion 
 5.Division (A/B)
 6.Division (B/A)
Opcion escogida: """
MENSAJE_SUMA = "El resultado de la suma es "
MENSAJE_RESTA = "El resultado de la resta es "
MENSAJE_MULTIPLICACION = "El resultado de la multiplicacion es "
MENSAJE_DIVISION = "El resultado de la division es "
MENSAJE_PREGUNTAS = " Ahora continuaremos con unas preguntas, ¿deseas continuar? "
decisionContinuacion = "1.Si        2. NO  R/="
MENSAJE_DESPEDIDA = "Gracias por utlizar este servicio para sus operaciones, vuelva pronto."
PREGUNTA_MAYOR = "¿El numero A es mayor que el numero B?"
PREGUNTA_DIFERENTES = "¿Los numeros A y B son diferentes?"
# Codigo 
print (MENSAJE_BIENVENIDA)
numeroA = int and float (input(MENSAJE_NUMEROA))
print (numeroA)
numeroB = int and float (input (MENSAJE_NUMEROB))
print (numeroB)
print (MENSAJE_OPCIONES)
opciones = int (input (listaOpciones))
print (opciones)
suma = numeroA + numeroB
if (opciones == 1) : print (MENSAJE_SUMA, suma)
resta2 = numeroA - numeroB
if (opciones == 2) : print (MENSAJE_RESTA, resta2)
resta3 = numeroB - numeroA 
if (opciones == 3) : print (MENSAJE_RESTA, resta3)
multiplicacion = numeroA * numeroB 
if (opciones == 4) : print (MENSAJE_MULTIPLICACION, multiplicacion)
division5 = numeroA / numeroB
if (opciones == 5) : print (MENSAJE_DIVISION, division5)
division6 = numeroB / numeroA
if (opciones == 6) : print (MENSAJE_DIVISION, division6)
print (MENSAJE_PREGUNTAS)
decision = int (input(decisionContinuacion))
print (decision)
isMayorQue = numeroA > numeroB
isDiferente = numeroA != numeroB
if (opciones == 1) : print ("#"*15, "Primera pregunta", "#"*15)
if (opciones == 1) : print (PREGUNTA_MAYOR, isMayorQue)
if (opciones == 1) : print ("#"*15, "Segunda pregunta", "#"*15)
if (opciones == 1) : print (PREGUNTA_DIFERENTES, isDiferente)
if (opciones == 1) : print ("#"*15, " Finalizado", "#"*15)
if (opciones == 1) : print (MENSAJE_DESPEDIDA)
if (opciones == 2) : print (MENSAJE_DESPEDIDA)