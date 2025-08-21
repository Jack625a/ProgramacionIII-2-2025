#entradas de datos por teclado
#input() => todo dato que recibe se convierte en cadena de caracteres
nombre=input("Ingrese su nombre: ")
celular=int(input("Ingrese su celular: "))
#Operaciones de entrada de datos
#1. Conversion de un input a valores numericos
#1.1. Valor numerico entero int()
edad=int(input("Ingrese su edad: "))
#1.2. Valor numerico decimal float()
precio=float(input("Ingrese el precio: "))


#Condicionales: Estructuras de control basado en condiciones
#2 CAMINOS POSIBLES 
#1 QUE SE CUMPLA LA CONDICION  VERDADERO
#2 QUE NO SE CUMPLA LA CONDICION FALSO
#if 

#MULTIPLES CONDICIONES
#elif
numero1=15
numero2=18
if numero1>=numero2:
    print("El numero mayor es",numero1)
else:
    print("El numero mayor es", numero2)

#Eje 1. Mostrar el mayor de tres numeros
num1=float(input("Ingrese un numero: "))
num2=float(input("Ingrese un numero: "))
num3=float(input("Ingrese un numero: "))
if num1>num2 and num1>num3:
    print("El numero mayor es ",num1)
elif num2>num1 and num2>num3:
    print("El numero mayor es ",num2)
elif num1==num2==num3:
    print("Los numeros son iguales")
else:
    print("El numero mayor es ",num3)
