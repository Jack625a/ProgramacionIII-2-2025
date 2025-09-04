#CREAR LA CLASE FIGURAS GEOMETRICAS
#SUBCLASES  CUADRADO, RECTANGULO TRINGULO,CIRCULO
#Paso 1. definir la clase
class FigurasGeometricas:
    #Paso 2. inicializar el constructor
    def __init__(self,nombre):
        self.nombre=nombre
    #Accion 
    def calcularArea(self):
        print(f"AREA DE LA FIGURA {self.nombre}")
    def calcularPerimetro(self):
        print(f"PERIMETRO DE LA FIGURA {self.nombre}")
    def calcularVolumen(self):
        print("Calculo del volumen")

class Circulo(FigurasGeometricas):
    def __init__(self,nombre,radio):
        super().__init__(nombre)
        self.radio=radio
    #herencia de la accion 
    def calcularArea(self):
        return 3.1416*self.radio**2

class Cuadrado(FigurasGeometricas):
    def __init__(self,nombre,lado):
        super().__init__(nombre)
        self.lado=lado
    def calcularArea(self):
        return self.lado*self.lado

class Rectangulo(FigurasGeometricas):
    def __init__(self,nombre,base,altura):
        super().__init__(nombre)
        self.base=base
        self.altura=altura
    def calcularArea(self):
        return self.base*self.altura

class Triangulo(FigurasGeometricas):
    def __init__(self,nombre,base,altura):
        super().__init__(nombre)
        self.base=base
        self.altura=altura
    def calcularArea(self):
        return (self.base*self.altura)/2
    def calcularPerimetro(self):
        if self.nombre=="Triangulo Equilatero":
            lado=float(input("Ingres un lado del triangulo: "))
            resultado=lado*3
            print(f"El area del {self.nombre} es {resultado}")
        elif self.nombre=="Triangulo Escaleno":
            lado1=float(input("Ingrese el primer lado del triangulo: "))
            lado2=float(input("Ingrese el segundo lado del triangulo: "))
            lado3=float(input("Ingrese el tercer lado del triangulo"))
            resultado=lado1+lado2+lado3
            print(f"El area del {self.nombre} es {resultado}")
        elif self.nombre=="Triangulo Isoceles":
            ladoIgual=float(input("Ingrese el lado que es igual del triangulo: "))
            ladodiferente=float(input("Ingrese el lado diferentes del triangulo: "))
            resultado=(ladoIgual*2)+ladodiferente
            print(f"El area del {self.nombre} es {resultado}")
        else:
            print("Triangulo invalido...")
    
    
    
#class Triangulo2:
 #   def calcularArea(self):
  #      return "Area Triangulo"
    
    
triangulo=Triangulo("Triangulo Equilatero",15,20)
print(triangulo.calcularArea())
triangulo.calcularPerimetro()
triangulo2=Triangulo("Triangulo Escaleno",20,18)
triangulo2.calcularPerimetro()
triangulo2.calcularArea()
triangulo2.calcularVolumen()