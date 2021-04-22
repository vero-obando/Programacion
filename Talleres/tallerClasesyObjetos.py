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
        '''
        La clase estudiante tiene atributos de edad, nombre, ID, carreray semestre.
        Tiene la funcion de ver la cantidad de tiempo de una materia.
        '''
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
        '''
        La clase nutricionista tiene atributos de edad, nombre y universidad.
        Tiene la accion de calcular el IMC.
        '''
        self.edad = edadUsuario
        self.nombre = nombreUsuario
        self.universidad = universidadUsuario
    
    def calculoIMC (self, peso, altura):
        imc = peso / (altura**2)
        print (f'Soy {self.nombre} y mi IMC es {imc}')

# Punto 4
class Canguro ():
    def __init__ (self, edadCanguro, nombreCanguro, idCanguro):
        '''
        La clase canguro tiene atributos de edad, nombre y ID.
        Tiene la accion de ver la cantidad de saltos dados.
        '''
        self.edad = edadCanguro
        self.nombre = nombreCanguro
        self.id = idCanguro
    
    def saltos (self, cantidadSaltos):
        for i in range (cantidadSaltos):
            print (f'Soy {self.nombre} el canguro y he dado {i+1} saltos')

# Punto 5 
class Guitarra ():
    def __init__ (self, colorEntrada, tipoEntrada, marcaEntrada):
        '''
        La clase guitarra tiene atributos de color, tipo y marca.
        Tiene la accion de interpretar una cancion.
        '''
        self.tipo = tipoEntrada
        self.color = colorEntrada
        self.marca = marcaEntrada
    
    def interpretacion (self, cancion):
        print (f'En la guitarra {self.tipo}, se va a interpretar la cancion {cancion}')

