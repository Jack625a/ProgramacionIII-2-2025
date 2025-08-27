#conjunto de codigo reutilizable
#def nombreFuncion():
#Funciones sin parametros
def bienvenida():
    print("Hola bienvenido")


bienvenida()
bienvenida()
bienvenida()

#Funciones con parametros
def sumar(a,b):
    return a+b

print(sumar(8,5))
print(sumar(11,8))

def restar(x,y):
    return x-y

def multiplicar(num1,num2):
    return num1*num2

def dividir(i,o):
    return i/o

#eJ 1. CREAR UNA CALCULADORA SIMPLE 
while True:
    print("Calculadora Simples")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion=int(input("quese operacion desea realizar?: "))
    a=float(input("Ingrese un numero: "))
    b=float(input("Ingrese un numero: "))
    if opcion==1:
        print("La suma es: ",sumar(a,b))
    elif opcion==2:
        print("La resta es: ",restar(a,b))
    elif opcion==3:
        print("La multiplicacion es: ",multiplicar(a,b))
    elif opcion==4:
        print("La division es ",dividir(a,b))
    elif opcion==5:
        print("Gracias por utlizar la calculadora...")
        break
    else:
        print("Error opcion invalida")

