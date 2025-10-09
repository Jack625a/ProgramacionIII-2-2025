#1. Importacion
import flet as ft
#IMPORTAR LAS PANTALLAS
from pantallas.pantalla1 import contenidoPantalla1
from pantallas.pantalla2 import contenidoPantalla2
from pantallas.pantalla3 import contenidoPantalla3
from pantallas.pantalla4 import contenidoPantalla4

#2. Funcion Principal
def main(page: ft.Page):
    #CABECERA
    page.appbar= ft.AppBar(
        title=ft.Text("Contenedores Tabs"),
        leading=ft.Icon(ft.Icons.LOOP_OUTLINED)
        )

    #PASO 1. CREAR LA VARIABLES OPCIONES (TABS)
    opciones=ft.Tabs(
        tabs=[
            ft.Tab(
                text="Opcion1",
                content=contenidoPantalla1(),
                icon=ft.Icons.KEY
            ),
            ft.Tab(
                text="Opcion2",
                content=contenidoPantalla2(),
                icon=ft.Icons.TIKTOK
            ),
            ft.Tab(
                text="Opcion 3",
                content=contenidoPantalla3(),
                icon=ft.Icons.FACEBOOK
            ),
            ft.Tab(
                text="Opcion 4",
                content=contenidoPantalla4(),
                icon=ft.Icons.HOME
            )
        ]
    )
    
    #3. Add - Interfaz
    page.add(
        opciones
    )

#3. Inicializacion
ft.app(main)
