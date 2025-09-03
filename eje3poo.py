#Realizar la clase empleado con los atributos 
#nombre, sueldo_base, puesto
#acciones: trabajar() - cobrar() - cobrarBeneficios() bono 30%
#Paso 1 definir la clase
class Empleado:
    #Paso 2. Definir el constructor y los atributos
    def __init__(self,nombre,sueldo_base,puesto,cuenta=0):
        self.nombre=nombre
        self.sueldo_base=sueldo_base
        self.puesto=puesto
        self.cuenta=cuenta

    #Paso3. Definir las acciones o metodos de la clase
    def trabajar(self):
        print(f"{self.nombre} esta trabajando...")
    def cobrar(self):
        self.cuenta=self.cuenta+self.sueldo_base
        print(f"Saldo disponible {self.cuenta}Bs - Titular: {self.nombre}")
    def cobrarBeneficios(self,porcentajeBono,horasExtra):
        calculoBono=self.sueldo_base*porcentajeBono
        calculoHorasExtra=(self.sueldo_base/30)*horasExtra
        print(f"Pago de Beneficios del empleado {self.nombre} - {calculoBono+calculoHorasExtra}Bs")
        self.cuenta=self.cuenta+calculoBono+calculoHorasExtra
        print(f" Saldo actual {self.cuenta}Bs Titular: {self.nombre}")

#CREACION DE SUBCLASES
#class nombreSubclase(ClasePadre):
class EmpleadoPorHoras(Empleado):
    #Definir el constructor y realizar la herencias de atributos
    def __init__(self,nombre,sueldo_base,puesto,horasTrabajadas,cuenta=0,):
        #Para heredar los atributos metod super()
        super().__init__(nombre,sueldo_base,puesto,cuenta)
        self.horasTrabajadas=horasTrabajadas
    #Acciones de la clase. 
    def cobrar(self,pago):
        self.cuenta=self.cuenta+(self.horasTrabajadas*pago)
        print(f"Pago a realizar: {self.horasTrabajadas*pago}Bs - Saldo: {self.cuenta}Bs")


empleado3=EmpleadoPorHoras("Ana",0,"Envios",10)
empleado3.cobrar(10)




#Paso 4. definir los objetos de la clase
empleado1=Empleado("Kevin Arroyo",2500,"Administracion")
empleado2=Empleado("Juan Perez",5000,"Jefe de Planta")

empleado1.cobrar()
empleado1.cobrar()
empleado1.cobrar()
empleado2.cobrar()

empleado1.cobrarBeneficios(0.3,8)
empleado2.cobrarBeneficios(0.3,10)



