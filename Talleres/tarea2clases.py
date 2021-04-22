# Crear clase animal y ponerle herencias
class Animal ():
    def __init__ (self, especieEntrada, habitatEntrada, nombreEntrada):
        self.especie = especieEntrada
        self.habitat = habitatEntrada
        self.nombre = nombreEntrada
    
    def mostrarAtributos (self):
        print (f'Mi nombre es {self.nombre}, vivo en {self.habitat} y soy un {self.especie}')

class Gato (Animal):
    def __init__ (self, especieEntrada, habitatEntrada, nombreEntrada, razaGato):
        Animal.__init__(self, especieEntrada, habitatEntrada, nombreEntrada)
        self.raza = razaGato
    
    def cambioArena (self, cantidadTiempo):
        print (f'Cada {cantidadTiempo} debes cambiarle la arena a tu gato {self.raza}')

class Leon (Animal):
    def cazar (self, presa):
        print (f'Por ser un animal carnivoro normalmente caza {presa}')

class Serpiente (Animal):
    def __init__ (self, especieEntrada, habitatEntrada, nombreEntrada, tipoSerpiente):
        '''
        En la clase serpinete, pide adicional el tipo, en este se debe poner si es venenosa 
        o si no lo es
        '''
        Animal.__init__(self, especieEntrada, habitatEntrada, nombreEntrada)
        self.tipo = tipoSerpiente
    
    def veneno (self):
        if (self.tipo == 'venenosa'):
            print ('Ten cuidado porque soy venenosa')
        else:
            print ('No soy venenosa, pero no me provoques')

