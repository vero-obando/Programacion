# Ejercicios condicionales 
# Solucion punto 1 
MENSAJE_BIENVENIDA = "Hola por favor ingrese dos numeros"
MENSAJE_NUMEROA = "El numero A sera : "
MENSAJE_NUMEROB = "El numero B sera : "
PREGUNTA_MAYOR = "El numero {} es mayor que el numero {}"
PREGUNTA_IGUALES = "Los numeros son iguales"
print(MENSAJE_BIENVENIDA)
numeroA = int (input (MENSAJE_NUMEROA))
numeroB = int (input (MENSAJE_NUMEROB))
if (numeroA > numeroB):
    print(PREGUNTA_MAYOR. format ( "A", "B"))
elif (numeroA < numeroB):
    print (PREGUNTA_MAYOR. format("B", "A"))
else:
    print (PREGUNTA_IGUALES)

# Solucion punto 2
MENSAJE_BIENVENIDA2 = "Hola, queremos evaluar tu edad"
MENSAJE_EDAD = "Por favor ingresa tu edad : "
MENSAJE_MENOR_EDAD = "Eres menor de edad"
MENSAJE_JOVEN = "Estas muy joven, disfrutalo"
MENSAJE_ADULTO = "Ya eres adulto, tienes responsabilidades que cumplir"
MENSAJE_ADULTO_MAYOR = "Cuentas como adulto mayor, te daran buenos beneficios"
print (MENSAJE_BIENVENIDA2)
edad = int (input (MENSAJE_EDAD))
menor = edad < 18
joven = 18 <= edad <= 25
adulto = 26 <= edad < 60
resultado = ""
if (menor):
    resultado = MENSAJE_MENOR_EDAD
elif (joven):
    resultado = MENSAJE_JOVEN
elif (adulto):
    resultado = MENSAJE_ADULTO
else:
    resultado = MENSAJE_ADULTO_MAYOR
print (resultado)

# Solucion punto 3 
MENSAJE_BIENVENIDA3 = "Hola, ahora queremos calcular cuanto tiempo ha pasado o pasara desde el año actual, hasta un año que desees"
MENSAJE_AÑO_ACTUAL = "Digita por favor el año actual : "
MENSAJE_AÑO = "Ahora, escribe un año que desees, sea pasado o futuro : "
MENSAJE_PASADO = "Han pasado {} años, desde el año {}"
MENSAJE_FUTURO = "Faltan {} años para llegar al año {}"
print (MENSAJE_BIENVENIDA3)
actual = int (input (MENSAJE_AÑO_ACTUAL))
otro = int (input (MENSAJE_AÑO))
resta1 = actual - otro
resta2 = otro - actual
if (actual > otro):
    print (MENSAJE_PASADO. format (resta1, otro))
else :
    print (MENSAJE_FUTURO. format (resta2, otro))

# Solucion punto 4
MENSAJE_BIENVENIDO4 = "Hola, vamos a calcular la distancia en varias unidades"
MENSAJE_CENTIMETROS = "Por favor ingrese la distancia en centimetros : "
LISTA_ELECCION = """ Escoge la unidad a la que desea convertir
1. Kilometros
2. Metros     R/: """
MENSAJE_KILOMETROS = "La distancia en kilometros es "
MENSAJE_METROS = "La distancia en metros es "
MENNSAJE_DESPEDIDA = "No escogiste ninguna de las opciones, adios"
print(MENSAJE_BIENVENIDO4)
centimetros = float (input (MENSAJE_CENTIMETROS))
lista = int (input (LISTA_ELECCION))
kilometros = centimetros * 100000
metros = centimetros * 100
if (lista == 1):
    print  (MENSAJE_KILOMETROS , kilometros)
elif (lista == 2) :
    print (MENSAJE_METROS , metros)
else:
    print (MENNSAJE_DESPEDIDA)
