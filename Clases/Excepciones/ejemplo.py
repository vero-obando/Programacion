#Para que el codigo no se estalle si se ingresa un valor invalido
isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        edad = int (input('Ingrese su edad :'))
        isCorrectInfo = True
    except ValueError:
        print('Ingresaste un dato no valido')

#Para cuando se va a buscar un archivo que no existe 
nombreArchivo = input('Ingrese el nombre del archivo que desea encontrar')
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    print(f'El archivo {nombreArchivo} no se ha encontrado')

# Indeterminada por dividir sobre cero
base = 4
divisor = 0
try:
    dividir = base/divisor
except ZeroDivisionError:
    print('El divisor ingresado es igual a cero, por esto NO se puede dividir')

#Crear errores 
nombre = 'Veronica'
print (nombre.isalpha())
assert(nombre.isalpha())

isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        nombre = input('Ingrese su nombre :')
        assert(nombre.isalpha())
        isCorrectInfo = True
    except AssertionError:
        print('Ingresaste un dato no valido')

isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        edad = int (input('Ingrese su edad :'))
        assert(edad >= 18)
        isCorrectInfo = True
    except AssertionError:
        print('Los menores de edad no pueden acceder')
    except ValueError:
        print('Las edades son numeros enteros')

#Para cuando el indice de una lista no existe
listas = [2,3,4,5]
try:
    listas[5]
except IndexError:
    print('El indice no se encuentra en la lista')
