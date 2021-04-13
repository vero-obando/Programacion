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
