# Punto 1
class Torta ():
    def __init__(self, formaEntrada, saborEntrada, alturaEntrada):
        '''
        La clase torta tiene atributos de forma, sabor y altura en cm.
        Tiene la funcion de mostrar atributos
        '''
        self.forma = formaEntrada
        self.sabor = saborEntrada
        self.altura = alturaEntrada
    
    def mostrarAtributos (self):
        print (f'''La torta es de forma {self.forma},
            tiene sabor a {self.sabor} y 
            su altura es de {self.altura} cm
        ''')

# Punto 2
class Estudiante ():
    def __init__ (self, edadEntrada, nombreEntrada, idEntrada, carreraEntrada, semestreEntrada):
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.id = idEntrada
        self.carrera = carreraEntrada
        self.semestre = semestreEntrada
    
    def estudiarMateria (self, materia, cantidadTiempo):
        print (f'Hola soy {self.nombre} y voy a estudiar {materia} en {cantidadTiempo} horas')

# Punto 3
class Nutricionista ():
    def __init__ (self, edadUsuario, nombreUsuario, universidadUsuario):
        self.edad = edadUsuario
        self.nombre = nombreUsuario
        self.universidad = universidadUsuario
    
    def calculoIMC (self, peso, altura):
        imc = peso / (altura**2)
        print (f'Soy {self.nombre} y mi IMC es {imc}')

# Punto 4
class Canguro ():
    def __init__ (self, edadCanguro, nombreCanguro, idCanguro):
        self.edad = edadCanguro
        self.nombre = nombreCanguro
        self.id = idCanguro



# Punto 5 
