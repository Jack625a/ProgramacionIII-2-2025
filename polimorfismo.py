#Capacidad de que diferentes clases usen un mismo metodo
class Animal:
    def __init__(self,tipo):
        self.tipo=tipo
    def comer(self):
        return f"Esta comiendo el {self.tipo}"

class Perro(Animal):
    def __init__(self,tipo,nombre,edad):
    #Herencia de atributos
        super().__init__(tipo)
        self.nombre=nombre
        self.edad=edad
    def comer(self):
        return f"Esta comiendo carne el {self.tipo}"

class Gato(Animal):
    def __init__(self,tipo,nombre,raza):
        super().__init__(tipo)
        self.nombre=nombre
        self.raza=raza
    def comer(self):
        return f"Esta comiendo el {self.tipo}"
    
class Veterinario:
    def atender(self,animal):
        print("Atendiendo al ",{animal})

#Comunicacion entre clases
perro=Perro("Perro","Huellitas",2)
gato=Gato("Gato","Peluza","Angora")
gallo=Animal("Gallo")
tigre=Animal("tigre")


animales=[perro,gato,gallo,tigre]
for animal in animales:
    print(animal.comer())

veterinario=Veterinario()

#Concepto del polimorfismo
veterinario.atender(perro.tipo)
veterinario.atender(gato.tipo)
veterinario.atender(tigre.tipo)
veterinario.atender(gallo.tipo)

#print(perro.comer())
#print(gato.comer("Pollo"))