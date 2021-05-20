import sys 
nombre = input ('Ingrese su nombre: ')
edad = int (input('Ingrese su edad: '))
estatura = float (input('Ingrese su estatura: '))

# Crear archivo si no existe
nombreArchivo = 'estudiantes.txt'
try:
    archivo = open(nombreArchivo)
    print('1')
except FileNotFoundError:
    archivo = open(nombreArchivo, 'w', encoding= 'UTF-8')
    descripcion = 'Archivo de datos de estudiantes'
    archivo.writelines(descripcion)
    sys.exit(1)
# Escribir en el archivo
archivo = open(nombreArchivo, 'a')
linea ='\nnombre: '+ nombre + ' edad: '+ str(edad) + ' estatura: '+ str(estatura)
archivo.writelines(linea)
archivo.close()
# Leer el archivo
with open(nombreArchivo, 'r') as reader:
    for line in reader:
        print(line)
