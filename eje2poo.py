#PASO 1. DEFINIR LA CLASE
class Calculadora:
    #PASO 2. INICIALIZAR EL CONSTRUCTOR -- PROPIEDADES
    def __init__(self,pantalla,marca,tipo):
        self.pantalla=pantalla
        self.marca=marca
        self.tipo=tipo
    #PASO 3. DEFINIR LAS ACCIONES O METODOS
    def sumar(self,numero1,numero2):
        return numero1+numero2
    def restar(self,a,b):
        return a-b
    def multiplicar(self,a,b):
        return a*b
    def dividir(self,a,b):
        return a/b

calculadora1=Calculadora("digital","casio","cientifica")
print(calculadora1.sumar(5,9))
print(calculadora1.multiplicar(8,5))


#EjeExtra

while True:
    print("Calculadora Simple")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion=int(input("Que operacion desea realizar: "))

    if opcion==1:
        a=int(input("Ingrese un numero: "))
        b=int(input("Ingrese un numero: "))
        print(a,"+",b,"=",calculadora1.sumar(a,b))
    elif opcion==2:
        a=int(input("Ingrese un numero: "))
        b=int(input("Ingrese un numero: "))
        print(a,"-",b,"=",calculadora1.restar(a,b))
    elif opcion==3:
        a=int(input("Ingrese un numero: "))
        b=int(input("Ingrese un numero: "))
        print(a,"x",b,"=",calculadora1.multiplicar(a,b))
    elif opcion==4:
        a=int(input("Ingrese un numero: "))
        b=int(input("Ingrese un numero: "))
        print(a,"/",b,"=",calculadora1.dividir(a,b))
    elif opcion==5:
        print("Gracias por utilizar la calculadora...")
        break
    else: 
        print("Error opcion invalida...")