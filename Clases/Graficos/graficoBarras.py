# Como hacer un grafico de barras
import matplotlib.pyplot as plt
lenguajes = ['py','java','dart','ts','elixir']
encuesta = [50, 10,20,10,10]
# Crear
plt.bar(lenguajes, encuesta, width= 0.6, color= 'm')
# Titulo
plt.title('Lenguajes mas usados')
# Etiqueta de ejes
plt.xlabel('Lenguajes de programacion')
plt.ylabel('% de uso de lenguajes')
# Guardar
plt.savefig('graficoLenguajes.png')
# Mostrar
plt.show()
