# Punto 1
isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        nombre = input('Ingrese su nombre :')
        assert(nombre.isalpha())
        isCorrectInfo = True
    except AssertionError:
        print('Ingresaste un nombre no valido')

isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        peso = float (input('Ingrese su peso en kg: '))
        estatura = float (input('ingrese su estatura en m: '))
        imc = peso / (estatura**2)
        isCorrectInfo = True
    except ZeroDivisionError:
        print('Por favor vuelve a ingresar los datos, la estatura no puede ser cero')
    except ValueError:
        print('Los datos son en numeros')
print('Tu IMC es...', imc)

# Punto 2 
isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        parrafo = input ('Por favor ingrese un parrafo: ')
        assert(parrafo.endswith('.'))
        parrafo = parrafo.replace(',',' ')
        parrafo = parrafo[:-1]
        palabras = parrafo.split(' ')
        print(f'La palabra mas grande es "{max(palabras, key= len)}" y el menor es "{min(palabras, key=len)}"')
        isCorrectInfo = True
    except AssertionError:
        print('Por favor vuelva a ingresar el parrafo con terminacion en punto')

# Punto 3
import sys
nombreArchivo = 'mantenimientos.txt'
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    archivo = open(nombreArchivo, 'w', encoding= 'UTF-8')
    descripcionArchivo = 'Archivo para manejo de clientes'
    archivo.writelines(descripcionArchivo)
    sys.exit(1)
nombre = input('Ingrese el nombre del equipo medico: ')
descripcion = input ('De una corta descripcion del equipo: ')
precio = int(input('Ingrese el precio del mantenimiento: '))
archivo = open(nombreArchivo, 'a')
linea ='\nEquipo medico: '+ nombre + ' Descripcion: '+ descripcion + ' Precio: '+ str(precio)
archivo.writelines(linea)
archivo.close()

# funciones utiles relacionadas 

def validateFloat(pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = float (input(pregunta))
            isCorrectData = True
        except ValueError:
            print('datos incorrectos ingrese nuevamente')
    return valor

def validateString(pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = input(pregunta)
            assert(valor.isalpha())
            isCorrectData = True
        except AssertionError:
            print('datos incorrectos ingrese nuevamente')
    return valor 

def validateEndWith(strValidate, pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = input(pregunta)
            assert(valor.endswith(strValidate))
            isCorrectData = True
        except AssertionError:
            print(f'datos incorrectos ingrese nuevamente y recuerde que debe terminar con "{strValidate}" ')
    return valor 

def pedirDatosEPN():
    '''
    Se le pide al usuario el peso la estatura 
    y el nombre
    validando que la data este buena
    '''
    preguntaPeso = 'Ingrese su peso en kg :'
    preguntaEstatura = 'Ingrese su estatura en metros : '
    preguntaNombre = 'Ingrese su Nombre :'
    peso = validateFloat(preguntaPeso)
    estatura = validateFloat(preguntaEstatura)
    nombre = validateString (preguntaNombre)
    return peso,estatura, nombre
