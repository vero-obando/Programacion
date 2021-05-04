import matplotlib.pyplot as plt
tiempo = [0,1,2,3,4,5]
sensor = [4,5,6,8,9, 10]
plt.plot(tiempo,sensor,'--,r')
plt.title('Grafico sensor contra el tiempo')
plt.xlabel('Tiempo(s)')
plt.ylabel('Voltaje(v)')
plt.savefig('sensor.png')
plt.show()

# Nota: se le puede poner el simbolo para que se grafique('--'), si no se pone nada se grafica como una linea recta

# DICCIONARIO
diccionario = {}
diccionario['NombresEstudiantes'] = ['Andrea', 'Nicolle', 'Isabel', 'Santiago']
diccionario['EdadEstudiantes'] = [18,20,19,15]
diccionario['Peso'] = [60,55,70,78]
print(diccionario)

print(diccionario['NombresEstudiantes'][-1][-1],diccionario['EdadEstudiantes'][-1],diccionario['Peso'][-1])

