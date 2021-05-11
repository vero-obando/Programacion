# Grafico barras
import matplotlib.pyplot as plt
preguntaSnacks = '''Por favor ingrese su snack favorito 
R/: ''' 
preguntaPrecios = ''' Ahora ingresa su precio
R/: '''
snacks = []
precios = []
for i in range (5):
    snacksin = input (preguntaSnacks)
    snacks.append(snacksin)
    preciosin = float(input(preguntaPrecios))
    precios.append(preciosin)
plt.bar(snacks,precios, color= 'm')
plt.title('Snacks favoritos')
plt.xlabel('Snacks')
plt.ylabel('Precio')
plt.savefig('snacksFav.png')
plt.show()

# Grafico torta
preguntaCiudades = '''Ingresa una de tus ciudades favoritas
R/: '''
preguntaPoblacion = ''' Ingresa su respectiva poblacion
R/:'''
ciudades = []
poblacion = []
for i in range (5):
    ciudadIn = input (preguntaCiudades)
    ciudades.append(ciudadIn)
    poblacionIn = int(input(preguntaPoblacion))
    poblacion.append(poblacionIn)

def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento

    for i in range (len(labels)):
        porcentaje = round(sizes[i]/acumulador*100)
        ciudades[i] += indicador+str(porcentaje) +'%'

maximo = max(poblacion)
ubicacion = poblacion.index(maximo)
pieExplode = [0,0,0,0,0]
pieExplode [ubicacion]= 0.1

etiquetarElementosPorcentuales(poblacion,ciudades)
plt.pie(poblacion, labels= ciudades, explode= pieExplode )
plt.title ('Ciudades favoritas')
plt.savefig('ciudadesFav.png')
plt.show()
