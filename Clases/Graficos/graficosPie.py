# Grafico de torta
import matplotlib.pyplot as plt
# Creamos los labels, sizes y explode
# labels: nombres porciones de la torta
pieLabels = ['python','java','dart','js']
# Sizes: los tamaños de la torta
sizes = [50,25,15,10]
# Explode: que tan alejado esta la torta, para resaltar la informacion
pieExplode = [0,0,0.1,0]

# Varias formas
# Primera forma
plt.pie(sizes, labels= pieLabels)
plt.title('Uso de lenguajes de programacion')
plt.savefig('tortasLenguajes.png')
plt.show()

# Segunda forma, con explode
plt.pie(sizes, labels= pieLabels, explode= pieExplode)
plt.title('Uso de lenguajes de programacion')
plt.savefig('tortasLenguajes.png')
plt.show()

# Tercera forma, con sombra
plt.pie(sizes, labels= pieLabels, explode= pieExplode, shadow= True)
plt.title('Uso de lenguajes de programacion')
plt.savefig('tortasLenguajes.png')
plt.show()

# Cuarta forma, cambio de angulo
plt.pie(sizes, labels= pieLabels, explode= pieExplode, shadow= True, startangle= 45)
plt.title('Uso de lenguajes de programacion')
plt.savefig('tortasLenguajes.png')
plt.show()

# FUNCION PARA ADICIONAR PORCENTAJES
def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento

    for i in range (len(labels)):
        pieLabels[i] += indicador+str(sizes[i]/acumulador*100) +'%'

# Quinta forma, mostrando porcentaje
etiquetarElementosPorcentuales(sizes,pieLabels,'->')
plt.pie(sizes, labels= pieLabels, explode= pieExplode, shadow= True)
plt.title('Uso de lenguajes de programacion')
plt.savefig('tortasLenguajes.png')
plt.show()

