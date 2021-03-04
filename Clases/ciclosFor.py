# Rangos comienzan desde cero 
for iteracion in range (10):
    print (iteracion)
print ('#'*60)
for iteracion in range (10):
    print (iteracion + 1)
print ('#'*60)
# El 1 entra en el rango, el 11 no 
for iteracion in range (1,11):
    print (iteracion)
# Saltos en el rango 
print ('#'*60)
for iteracion in range (1,11,2):
    print (iteracion)
print ('#'*60)
residuo = 5%4
print (residuo)
residuo = 4%4
print (residuo)
# Mostrar solo los pares 
print ('#'*60)
for iteracion in range (1,11):
    if (iteracion%2 == 0):
        print(iteracion)
# Mostrar solo los impares 
print ('#'*60)
for iteracion in range (1,11):
    if (iteracion%2 != 0):
        print (iteracion)
# Decir cual es impar y cual par 
print ('#'*60)
for iteracion in range (1,11):
    if (iteracion%2 == 0):
        print (iteracion, 'es un numero par')
    else:
        print (iteracion, 'es un numero impar')
# Con el usuario
print ('#'*60)
rango = int (input ('ingrese el rango maximo'))
opcion = int (input('''
1. Ver solo impares 
2. Ver solo pares
3. Ver las dos clasificaciones 
n. cualquier numero para no mostrar nada 
''' ))

if (opcion == 1):
    for iteracion in range (1, rango + 1):
        if (iteracion%2 != 0):
            print (iteracion)
elif (opcion == 2):
    for iteracion in range (1, rango + 1):
        if (iteracion%2 == 0):
            print (iteracion)
elif (opcion == 3):
    for iteracion in range (1, rango + 1):
        if (iteracion%2 == 0):
            print (iteracion, 'es un numero par')
    else:
        print (iteracion, 'es un numero impar')
else:
    print ('Mostrando nada')
