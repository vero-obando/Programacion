# Punto 1
class Persona ():
    def __init__ (self, idPersona, nombrePersona, edadPersona):
        self.id = idPersona
        self.nombre = nombrePersona
        self.edad = edadPersona
    
    def hablar (self, mensaje):
        print (mensaje)
    
    def caminar (self, cantidadPasos):
        print (f'Hola soy {self.nombre} y he caminado {cantidadPasos} pasos')

# Punto 2 
class Doctor (Persona):
    def __init__ (self, idPersona, nombrePersona, edadPersona, especialidadMedicina):
        Persona.__init__(self, idPersona, nombrePersona, edadPersona)
        self.especialidad = especialidadMedicina
    
    def tratarEnfermedad (self, enfermedad):
        print (f'Soy {self.nombre} y procedo a tratar {enfermedad}')

# Punto 3
class Nutricionista (Persona):
    def __init__ (self, idPersona, nombrePersona, edadPersona, universidadEgresado):
        Persona.__init__(self, idPersona, nombrePersona, edadPersona)
        self.universidad = universidadEgresado
    
    def calculoIMC (self, peso, altura):
        imc = peso / (altura**2)
        print (f'El IMC del paciente es {imc}')

# Punto 4
class Abogado (Persona):
    def __init__ (self, idPersona, nombrePersona, edadPersona, universidadEgresado, especialidadDerecho):
        Persona.__init__(self, idPersona, nombrePersona, edadPersona)
        self.universidad = universidadEgresado
        self.especialidad = especialidadDerecho
    
    def representacion (self, nombreCliente, casoCliente):
        print (f'Procedo a representar al cliente {nombreCliente} en el caso {casoCliente}')


