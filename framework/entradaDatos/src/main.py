#Importacion framework
import flet as ft


#funcion principal
def main(page: ft.Page):

    nombre=ft.TextField(label="Ingrese su nombre: ", icon=ft.Icons.PERSON)
    carrera=ft.TextField(label="Ingrese su carrera: ", icon=ft.Icons.HOUSE)
    correo=ft.TextField(label="Ingrese su correo", icon=ft.Icons.EMAIL)
    contraseña=ft.TextField(label="Ingrese su contraseña", password=True, can_reveal_password=True)
    celular=ft.TextField(label="Ingrese su celular", keyboard_type=ft.KeyboardType.PHONE)
    
    #componentes de la interfaz
    page.add(
        nombre,
        carrera,
        correo,
        contraseña,
        celular
    )

#Inicializacion de la app
ft.app(main)
