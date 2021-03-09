nombres = []
print (type(nombres))
print (nombres)
nombres = ['Santi','Samuel', 'Aleja','Elsa']
print (nombres)
print (nombres[2])
nombres.append ('Mauricio')
print (nombres)
print (nombres [2])
edades = [18,19,20,17]
estaturas = [1.62, 1.80, 1.67, 1.98]
# Al ultimo 
print (edades[-1])
# Primeros elementos, incluye al primero pero no al segundo 
print (edades [0:2])
print (edades[:3])
# Hasta terminar 
print (edades [2:])
# Todo 
print (edades [:])
print (edades)
# Ordenar lista 
edades.sort()
print (edades)
edades.sort (reverse=True)
print (edades)
mayor = max(edades)
print (mayor)
menor = min(edades)
print (menor)
# Como contamos cuantos elementos hay 
largoListaEdades = len(edades)
print (largoListaEdades)
# Como sumamos elementos
sumaEdades = sum(edades)
print (sumaEdades)
# Como calculo el promedio
promedioEdades = sumaEdades/largoListaEdades
print (promedioEdades)
# Eliminar un elemento 
edades.pop(2)
print (edades)

# Ciclo for y las listas
largoListaEdades = len(edades)
for indice in range (largoListaEdades):
    print ('estoy en la posicion',
    indice, 'valgo',
    edades[indice])
largoListaNombres = len(nombres)
for indice in range (largoListaNombres):
    print (nombres [indice])

posicionesConValoresPares = []
largoListaEdades = len(edades)
for posicion in range (largoListaEdades):
    if(edades[posicion]%2 == 0):
        posicionesConValoresPares.append(posicion)

print (edades)
print (posicionesConValoresPares)

# Solo cuando les interese mostrar la lista
for edad in edades:
    print (edad)
for nombre in nombres:
    print (nombre)
    print (posicion)
    posicion+=1

posicion = 0 
posicionesPares = []
for edad in edades:
    if (edad%2 == 0 ):
        posicionesPares.append(posicion)
    posicion+=1
print (posicionesPares)


