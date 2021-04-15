# Clase sobre mi mascota favorita 
class Perro ():
    def __init__ (self, nombreEntrada, mesesEntrada, razaEntrada):
        '''
        Esta es la clase perro, pide atributos de nombre, raza y meses de edad.
        Tiene las acciones de:
        *Mostrar atributos
        *Vacunas
        *Cantidad comida 
        *Salidas 
        '''
        print ('Hola soy tu perro, aqui puedes saber mi informacion')
        self.raza = razaEntrada
        self.nombre = nombreEntrada
        self.meses = mesesEntrada
    
    def mostrarAtributos (self):
        print(f'''Mi nombre es {self.nombre}
        Soy de raza {self.raza}
        Tengo {self.meses} meses
        ''')
    
    def vacunas (self):
        print (f'Hola soy {self.nombre} tu perro... ')
        if (self.meses == 1):
            print ('Al mes y medio me debes poner la primovacunacion')
        elif (self.meses == 2):
            print ('Ya debo tener la primovacunacion y me debes poner la polivalente')
        elif (self.meses == 3):
            print ('Ya debo tener la primovacunacion, la polivalente y me debes poner el recordatorio de la polivalente')
        elif (self.meses == 4):
            print ('Ya debo tener la primovacunacion, la polivalente, el recordatorio de la polivalente y me debes poner la de la rabia')
        else:
            print ('Debo tener ya todas las vacunas y recuerda anualmente ponerme el recordatorio de la rabia y la polivalente')
    
    def cantidadComida (self, cantidad):
        print (f'Hola soy {self.nombre} tu perro... Cada dia debo comer {cantidad} veces, dividelas bien por favor')
    
    def salidas (self, veces):
        print (f'Hola soy {self.nombre} tu perro... Me encanta que salgamos a pasear {veces} veces al dia')

perro1 = Perro('pola',1,'pincher')
perro2 = Perro('frida',2,'labrador')
perro3 = Perro('luna', 3, 'pastor aleman')
perro4 = Perro('limber',4,'chiguagua')
perro5 = Perro('isis',5,'lobo siberiano')

perro1.mostrarAtributos()
perro1.vacunas()
perro2.vacunas()
perro3.vacunas()
perro4.vacunas()
perro5.vacunas()

perro2.cantidadComida(3)
perro3.salidas(4)
