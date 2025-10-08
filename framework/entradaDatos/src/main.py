#Importacion framework
import flet as ft


#funcion principal
def main(page: ft.Page):

    nombre=ft.TextField(label="Ingrese su nombre: ", icon=ft.Icons.PERSON)
    carrera=ft.TextField(label="Ingrese su carrera: ", icon=ft.Icons.HOUSE)
    correo=ft.TextField(label="Ingrese su correo", icon=ft.Icons.EMAIL)
    contraseña=ft.TextField(label="Ingrese su contraseña", password=True, can_reveal_password=True)
    celular=ft.TextField(label="Ingrese su celular", keyboard_type=ft.KeyboardType.PHONE)
    
    #Contenedores
    #1. contenedores Horizontales
    contenedorHorizontal=ft.Row(
        [
            nombre,carrera,correo,contraseña,celular
        ],
        auto_scroll=True,
        scroll=ft.ScrollMode.AUTO, #Activacion del scroll
        #width=500
        spacing=20
    )
    #2. Contenedor Vertical
    contenedorVertical=ft.Column(
        [
            correo,
            celular,
            contenedorHorizontal
        ],
        width=400
    )


    #componentes de la interfaz
    page.add(
        nombre,
        carrera,
        correo,
        contraseña,
        celular,
        contenedorHorizontal,
        contenedorVertical
    )

#Inicializacion de la app
ft.app(main)
