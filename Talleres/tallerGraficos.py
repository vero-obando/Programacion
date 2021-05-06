# Grafico de barras sobre niveles de ingreso 2020
import matplotlib.pyplot as plt
ingresos = [700000,800000,500000,900000, 450000, 780000]
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
plt.bar(meses, ingresos, color= 'm')
plt.title('Ingresos primer semestre 2020')
plt.xlabel('Meses')
plt.ylabel('Ingresos (pesos)')
plt.savefig('Ingresos2020-1.png')
plt.show()

ingresos2 = [750000,600000,900000,800000, 760000, 950000]
meses2 = ['Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
plt.bar(meses2, ingresos2, color= 'r')
plt.title('Ingresos segundo semestre 2020')
plt.xlabel('Meses')
plt.ylabel('Ingresos (pesos)')
plt.savefig('Ingresos2020-2.png')
plt.show()

# Grafico torta sobre 5 ciudades de Colombia
pieLabels = ['Medellin','Cali', 'Bogota', 'Barranquilla', 'Nariño']
sizes = [2569000000, 2228000000, 7181000000, 1206000000, 1631000000]
pieExplode = [0,0,0.1,0,0]

def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento

    for i in range (len(labels)):
        porcentaje = round(sizes[i]/acumulador*100)
        pieLabels[i] += indicador+str(porcentaje) +'%'

etiquetarElementosPorcentuales(sizes, pieLabels)
plt.pie(sizes, labels= pieLabels, explode= pieExplode, shadow= True)
plt.title('Habitantes en ciudades de Colombia')
plt.savefig('habitantes.png')
plt.show()

