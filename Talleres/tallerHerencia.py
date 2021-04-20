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

