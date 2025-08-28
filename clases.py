#Clases: class NombreClase
#Metodos o acciones (def nombreAccion())
#Funcion del constructor
#def __init__()
#identificador de propiedades (self)
#PASO 1. DEFINIR LA CLASE
class Persona:
    #Paso 2. Inicializar el constructor - parametros
    def __init__(self,nombre,edad,ci):
        self.nombre=nombre
        self.edad=edad
        self.ci=ci
    #Paso 3. Definir las acciones o metodos
    def dormir(self):
        print(self.nombre," Esta durmiendo...")
    def comer(self,comida):
        print(self.nombre," Esta comiendo ",comida)

#PASO 4. CREAR LOS OBJETOS DE LA CLASE
persona1=Persona("Kevin Arroyo",29,1234567)
persona2=Persona("Juan Perez",25,7894552)

persona1.dormir()
persona2.comer("Pan")