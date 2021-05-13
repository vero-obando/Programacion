# Repaso
texto = 'Hola espero todo ande bien'
lista = [1, 432, 53, 2, 4]
lista.sort()
print (lista)
lista.pop(2)
for elemento in lista:
    print(elemento)
for i in range (len(lista)):
    print(lista[i])

# Strings parecido a lista
for letra in texto:
    print(letra)

print(texto[1])

# Quitar algo del texto
palabras = texto.split(' ')
print(palabras)
print(type(palabras))
eliminarE = texto.split('e')
print(eliminarE)
datos = 'nombre;apellido;edad'
print (datos.split(';'))

# Unir la lista en un texto 
uniendo = 'i'.join(eliminarE)
print(uniendo)
info = ' '.join(datos.split(';'))
print(info)

# Comparar string con otro
listaNombres = ['Laura', 'Juan', 'Mario','Katherine', 'daniel']
print(max(listaNombres, key= len))

# Volver todo en mayuscula
respuesta = input('Ingrese Si o No: ')
print(respuesta.upper())
if respuesta.upper() == 'SI':
    print('Hola bienvenido al código')
else:
    print('chao!!')

# Poner primera letra en mayuscula
nombre = input('Ingrese su nombre: ')
print(nombre.capitalize())
print(type(nombre))

# Poner letras en minusculas 
correo = 'ESPERO QUE ESTES BIEN'
print (correo.casefold().capitalize())
# Dos nombres con la primera letra en mayuscula
nombre = 'maria alejandra'
nombres = nombre.split(' ')
nombre= ''
for elemento in nombres:
    nombre += elemento.capitalize() +' '
print(nombre)

# Centrar strings 
saludo = 'Hola como estas?'
nombre = 'Maria Alejandra'
print(saludo.center(50))
print(nombre.center(50))

# Contar el numero de palabras en un string 
enunciado = 'Hola hola ya me cansé de decir tantos Hola pero como vamos hola'
print (enunciado.upper().count('HOLA'))
# Posicion de una letra o palabra en el string
print (enunciado.find('decir'))
print (enunciado[25:30])

# Cambiar palabras en un string
txt = 'me gusta programar en java'
print (txt.replace('java', 'python'))

# Saber si un string es numerico 
numeroId = '123124'
print(numeroId.isnumeric())

# Saber si el parrafo termina en punto 
parrafo = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas debitis hic libero quos, aliquam nostrum officia! Unde, magnam ex? Vel aliquid ducimus aliquam error quod rem ut quos animi numquam.'
print (parrafo.endswith('.'))
