class Humano():
    def __init__ (self, nombreEntrada, edadEntrada, estaturaEntrada):
        '''
        Esta es la clase Humano y pide atributos de nombre, edad y estatura.
        Tiene las acciones de:
        * Hablar
        *Mostrar atributos 
        *Recorrer distancia
        *Ahorrar dinero 
        '''
        print ('Hola soy un humano nuevo')
        self.raza = 'Humano'
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.estatura = estaturaEntrada
        self.dinero = 0
    
    def hablar(self, mensaje):
        print(f'Hola soy {self.nombre} tengo un mensaje que decirte : ', mensaje)
    def mostrarAtributos (self):
        print (f'''Mi nombre es {self.nombre}
                    Mi estatura es {self.estatura}
                    Mi edad es {self.edad}
                    Tengo ahorrado {self.dinero}
        ''')
    def recorrerDistancia (self, distanciaMetros):
        for i in range (distanciaMetros):
            print (f'Hola soy {self.nombre} y he recorrido {i + 1 } metros')
    def ahorraDinero (self):
        preguntaIngresarMonto = 'Ingrese S--> para continuar añadiendo montos y N--> para finalizar : '
        preguntaMonto = 'Cuanto vas a ingresar?: '
        ingresarMontos =input(preguntaIngresarMonto)
        while(ingresarMontos != 'N'):
            monto = float(input(preguntaMonto))
            self.dinero = self.dinero + monto
            print(f'Soy {self.nombre} y tengo {self.dinero} pesos')
            ingresarMontos =input(preguntaIngresarMonto)
        return self.dinero

class Ingeniero (Humano):
    def __init__ (self, nombreEntrada, edadEntrada, estaturaEntrada, areaEntrada):
        Humano.__init__(self, nombreEntrada, edadEntrada, estaturaEntrada)
        self.area = areaEntrada

    def solucionarProblemas (self, problema):
        print (f'Hola soy un ingeniero y me llamo {self.nombre} y procedo a solucionar {problema}')

class Programador (Humano):
    def crearAlgoritmo (self, algoritmo):
        print (f'Hola soy {self.nombre} y procedo a resolver el algoritmo {algoritmo}')

class Biomedico (Ingeniero, Programador):
    def mantenimientoEquiposMedicos (self, nombreEquipo):
        print (f'Hola soy {self.nombre} y voy a arreglar el {nombreEquipo}')

class Abogado (Humano):
    def levantarAccionTutela (self, nombreCliente):
        print (f'Hola soy {self.nombre} y estoy representando a {nombreCliente}')


humano1 = Humano('daniel', 27, 1.67)
humano2 = Humano('vero', 18, 1.50)

humano1.hablar('Espero que esten muy bien')
humano2.hablar('Chao')
print (humano1.nombre)
print (humano2.nombre)
print (humano2.edad)
humano1.mostrarAtributos()
humano1.recorrerDistancia(25)
totalAhorrado = humano2.ahorraDinero()
humano2.mostrarAtributos()

biomedico1 = Biomedico('Karla',20,1.63,'Biomédicina')
biomedico1.recorrerDistancia(25)
biomedico1.mostrarAtributos()
biomedico1.mantenimientoEquiposMedicos('Electrocardiograma')

abogado1 = Abogado('Stiven',34,1.94)
abogado1.mostrarAtributos()
abogado1.levantarAccionTutela(biomedico1.nombre)
biomedico1.crearAlgoritmo('Fibonacci')
biomedico1.solucionarProblemas('Ocupación alta de UCIs')
print(biomedico1.area) 
