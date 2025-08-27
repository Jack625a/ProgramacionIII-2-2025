#Bucles: Ciclos repetitivos
#1. Bucles iterativos
#definidos en un rango especifico 
#for i in range(valorInicio,ValorFinal,conteo):
for i in range(1,11):
    print(i)

#Ej1. Mostrar los numero pares hasta 100
for pares in range(2,101,2):
    print(pares)

#Ej2. Mostrar los numeros impares hasta 100
for impares in range(1,101,2):
    print(impares)

#Ej 3. Mostrar la tabla de multiplicar de 8
for tabla in range(1,11):
    print(tabla,"x 5 =",tabla*5)

#Ej 4. Mostrar la tabla de multiplicar de N
#que el usuario decida que tabla mostrar


#2. Bucles condicionados while (romper bucle break)
# while (condicion):
#
contador=1
while contador<=10:
    print(contador)
    contador=contador+1

#Ej1. mostrar los numeros pares hasta el 100
paresW=2 #contador
while paresW<=100:
    print(paresW)
    paresW=paresW+2 #incremento

#Ej2. mostrar los numeros impares hasta el 100
imparesW=1
while imparesW<=100:
    print(imparesW)
    imparesW+=2

#Eje3. Tabla de multiplicar del 8
tabla8=1
while tabla8<=10:
    print("8x",tabla8,"=",tabla8*8)
    tabla8=tabla8+1

tablaN=int(input("Que tabla desea ver? "))
contador=1
while contador<=10:
    print(tablaN,"x",contador,"=",tablaN*contador)
    contador=contador+1

#while True:
while True:
    print("TABLA DE MULTIPLICAR N")
    print("100 para salir")
    tablaN=int(input("Que tabla desea ver? "))
    if tablaN==100:
        print("Gracias por utlizar el programa...")
        break
    else:
        contador=1
        while contador<=10:
            print(tablaN,"x",contador,"=",tablaN*contador)
            contador=contador+1