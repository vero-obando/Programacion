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
        peso = float (input('Ingrese su peso: '))
        estatura = float (input('ingrese su estatura: '))
        imc = peso / (estatura**2)
        isCorrectInfo = True
    except ZeroDivisionError:
        print('Por favor vuelve a ingresar los datos, la estatura no puede ser cero')
    except ValueError:
        print('Los datos son en numeros')
print('Tu IMC es...', imc)

# Punto 2 me falta la palabra mas grande y pequeña
isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        parrafo = input ('Por favor ingrese un parrafo: ')
        assert(parrafo.endswith('.'))
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
