#eje2. Dado 3 calificaciones calcular el promedio y determinar 
#el estado del estudiante
#1. 95 para arriba Excelente
#2. 81 a 94 Muy bien
#3. 71 a 80 Bien
#4. 61 a 70 Normal
#5. 51 a 60 Regular
#6. 51 para abajo Reprobado

nota1=float(input("Ingrese la primera nota: "))
nota2=float(input("Ingrese la segunda nota: "))
nota3=float(input("Ingrese la tercera nota: "))
promedio=(nota1+nota2+nota3)/3

if promedio>=95:
    print("Estado: Excelente - Nota: ",promedio)
elif promedio>=81 and promedio<95:
    print("Estado: Muy Bien - Nota: ",promedio)
elif promedio>=71 and promedio<81:
    print("Estado: Bien - Nota: ",promedio)
elif promedio>=61 and promedio<71:
    print("Estado: Normal - Nota: ",promedio)
elif promedio>=51 and promedio<61:
    print("Estado: Regular - Nota: ",promedio)
else:
    print("Estado: Reprobado - Nota: ",promedio)
