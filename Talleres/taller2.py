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
numeroA = int (input(MENSAJE_NUMEROA))
numeroB = int (input (MENSAJE_NUMEROB))
print (MENSAJE_OPCIONES)
opciones = int (input (listaOpciones))
suma = numeroA + numeroB
resta2 = numeroA - numeroB
resta3 = numeroB - numeroA 
multiplicacion = numeroA * numeroB 
division5 = numeroA / numeroB
division6 = numeroB / numeroA
resultado = ""
if (opciones == 1) : 
    resultado = MENSAJE_SUMA, suma
elif (opciones == 2) : 
    resultado = MENSAJE_RESTA, resta2
elif (opciones == 3) : 
    resultado = MENSAJE_RESTA, resta3
elif (opciones == 4) :
    resultado = MENSAJE_MULTIPLICACION, multiplicacion
elif (opciones == 5) :
    resultado = MENSAJE_DIVISION, division5
elif (opciones == 6) :
    resultado = MENSAJE_DIVISION, division6
print (resultado)
print (MENSAJE_PREGUNTAS)
decision = int (input(decisionContinuacion))
isMayorQue = numeroA > numeroB
isDiferente = numeroA != numeroB
if (decision == 1) :
    print ("#"*15, "Primera pregunta", "#"*15)
    print (PREGUNTA_MAYOR, isMayorQue) 
    print ("#"*15, "Segunda pregunta", "#"*15) 
    print (PREGUNTA_DIFERENTES, isDiferente)
    print ("#"*15, " Finalizado", "#"*15) 
    print (MENSAJE_DESPEDIDA)
elif (decision == 2):
    print (MENSAJE_DESPEDIDA)

