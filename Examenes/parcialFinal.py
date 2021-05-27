# Punto 1
import matplotlib.pyplot as plt
preguntaAlimentos = 'Ingrese un alimento favorito: '
preguntaPrecio = 'Ingrese su respectivo precio: '
alimentos = []
precios = []
for i in range (8):
    alimentosIn = input(preguntaAlimentos)
    alimentos.append(alimentosIn)
    preciosIn = float (input(preguntaPrecio))
    precios.append(preciosIn)
plt.bar(alimentos, precios, color= 'g')
plt.title('Alimentos favoritos')
plt.xlabel('Alimentos')
plt.ylabel('Precio')
plt.savefig('alimentosfav.png')
plt.show

# Punto 2
class Humano ():
    def __init__ (self, nombreIn, sexoIn, edadIn):
        self.nombre = nombreIn
        self.sexo = sexoIn
        self.edad = edadIn
    def hablar(self, mensaje):
        print(f'Hola soy {self.nombre} y te quiero decir que: ', mensaje)

class Doctor (Humano):
    def calcularIMC (self, peso, estatura):
        imc = peso / (estatura**2)
        print(f'El IMC del paciente es: ', imc)

humano1 = Humano('vero','femenino', 18)
humano1.hablar('eres la mejor')
doctor1 = Doctor('stefa','femenino', 26)
doctor1.calcularIMC(70, 1.60)

# Punto 3
isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        nombre = input('Ingrese su nombre: ')
        assert(nombre.isalpha())
        dolares = float(input('Por favor ingrese su dinero en dolares: '))
        euros = dolares * 0.82
        print(f'Hola soy {nombre} y tengo {euros} euros')
        isCorrectInfo = True
    except AssertionError:
        print('Ingresaste un nombre no valido')
    except ValueError:
        print('Datos incorrectos, ingreselos nuevamente')

# Punto 4
import sys
nombreArchivo = 'pacientes.txt'
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    archivo = open(nombreArchivo, 'w', encoding= 'UTF-8')
    descripcionArchivo = 'Clientes consultorio de neurología'
    archivo.writelines(descripcionArchivo)
    sys.exit(1)
nombre = input('Ingrese el nombre del paciente: ')
descripcion = input ('De una corta descripcion de su respectiva enfermedad: ')
precio = int(input('Ingrese el precio de la consulta : '))
archivo = open(nombreArchivo, 'a')
linea ='\n\nPaciente: '+ nombre + '\nDescripcion enfermedad: '+ descripcion + '\nPrecio consulta: '+ str(precio)
archivo.writelines(linea)
archivo.close()

# Mensaje despedida: Hola profe, se que no fui de las mas participativas en clase, pero te
#quiero agradecer porque realmente eres un gran profesor, personalmente tenia mucho miedo de esta materia
# y creo que gracias a tus explicaciones y a tu forma de ser todo se me hizo mas facil. Enserio muchisimas gracias por todo!!
