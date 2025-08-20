#Basicos de Python
#1. Variables -> Espacio reservado en la memoria
#2. Tipos de datos
#2.1. Tipos de datos simples (Numericos,Booleanos,Cadena de caracteres)
nombre="Kevin"
numero=45.7
encender=False
#2.2. Tipos de datos Complejos (Listas,Tuplas,Diccionarios)
#Listas ->Conjunto de datos ordenados o desornados - mutables - [valor,valor,valor]
colores=["Rojo","Verde","Amarillo","Cafe","Azul","Rosado"]
numeros=[5,8,4,6,9,10,7,1,10]
#operaciones basicas de una lista
#Mostrar el primer elemento de una lista [0]
print(colores[0])
print(numeros[0])
#Mostrar el numero 10 de la lista de numeros
print(numeros[5])
#Mostrar el ultimo elemento de una lista [-1]
print(colores[-1])
#Agregado de datos - "append" -> agrega un elemento al final de la lista
colores.append("Anaranjado")
print(colores)
print(colores[-1])
numeros.append(95)
print(numeros)
#Actualizacion de datos 
colores[1]="Blanco"
print(colores)
numeros[-1]=150
print(numeros)
#Eliminacion de datos
numeros.remove(10)
print(numeros)
#numeros.clear()
#print(numeros)
del numeros[7]
#Longitud de una lista ->cantidad de elemento que tiene una lista "len"
print(len(colores))
print(len(numeros))
#TUPLAS -> Conjunto de elementos ordenados o desordenados que 
# son inmutables es decir no se modifican a lo largo del codigo constantes 
# se define con (elemento,elemento,elemento)
codigos=(445,122,351,996,451)
#Diccionarios: Conjunto de elementos ordenados o desordenados que
# se representan por una clave y un valor {}

estudiantes={
    "nombre":"Kevin Arroyo",
    "codEstudiante":745222,
    "carrera":"Ingenieria de Sistemas",
    "celular":65402336
}

print(estudiantes)
#Operaciones de los diccionarios
#1.Acceder a los valores diccionario[clave]
print(estudiantes["codEstudiante"])
#Verificacion de valor existente (get)
print(estudiantes.get("edad","El valor no existe"))

print("AGREGADO DE DATOS")
#2. AGREGADO DE VALORES 
estudiantes["edad"]=29
estudiantes["correo"]="k@gmail.com"
print(estudiantes)

print("MODIFICACION DE DATOS")
#3. MODIFICACION DE VALORES
estudiantes["correo"]="ke@gmail.com"
print(estudiantes)

#ELIMINACION DE DATOS DEL DICCIONARIO
#1. ELIMINACION DE UNA CLAVE ESPECIFICA del
del estudiantes["correo"]
print(estudiantes)

#2.ELIMINACION DE UN VALOR
valor=estudiantes.pop("edad")
print(valor)
print(estudiantes)

#3. ELIMINACION DE TODO EL DICCIONARIO
estudiantes.clear()
print(estudiantes)

#DICCIONARIOS ANIDADOS
estudiantes2={
    "123":{
        "nombre":"Kevin Arroyo",
        "carrera":"Ingenieria de Sistemas",
        "correo":"k@gmail.com",
        "celular":65403254,
        "codEstudiante":123
    },
    "456":{
        "nombre":"Juan Perez",
        "carrera":"Ingenieria de Sistemas",
        "correo":"jua@gmail.com",
        "celular":73841123,
        "codEstudiante":456
    },
    "789":{
        "nombre":"Ana Perez",
        "carrera":"Ingenieria de Sistemas",
        "correo":"ana@gmail.com",
        "celular":69841123,
        "codEstudiante":789
    }
}

print(estudiantes2["123"]["nombre"])

#RECORRIDOS DE UN DICCIONARIO
print("RECORRIDO DE UN DICCIONARIO")
for codigo, datos in estudiantes2.items():
    print("codEstudiante",codigo)
    print("Nombre: ",datos["nombre"])
    print("Carrera: ",datos["carrera"])
    print("Celular: ",datos["celular"])
    print("Correo: ",datos["correo"])
    print("----------------------")

  

