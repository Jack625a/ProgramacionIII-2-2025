#IMPORTACION DEL FRAMEWORK
import flet as ft

#FUNCION PRINCIPAL 
def main(page: ft.Page):
    
    nombre=ft.Text("Kevin Arroyo Montaño", size=25)
    boton=ft.Button("Prueba Boton",bgcolor=ft.colors.GREEN_400)
    #COMPONENTES BASICOS DE LA INTERFAZ
    #1. BOTONES
    boton2=ft.CupertinoFilledButton(
        text="Boton Cupertino",
        icon=ft.Icons.LOCAL_PIZZA,
        icon_color=ft.Colors.WHITE,
    )
    boton3=ft.ElevatedButton(
        text="Boton Elevated",
        icon=ft.Icons.PERSON_PIN
    )
    boton4=ft.FilledButton(
        text="Boton Filled",
        icon=ft.Icons.MODE_EDIT_ROUNDED,
        bgcolor=ft.Colors.PURPLE_400,
        
    )
    botonFlotante=ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        mini=True,
        mouse_cursor=ft.MouseCursor.HELP
    )
    boton5=ft.FilledTonalButton(
        text="Boton tonal",
        icon=ft.Icons.TIKTOK
    )
    botonIcono=ft.IconButton(
        icon=ft.Icons.CAR_CRASH,
        bgcolor="#913052",
        icon_color=ft.Colors.WHITE
    )
    texto=ft.Text(
        value="Framework Flet",
        size=30,
        weight=ft.FontWeight.W_800,
        font_family="Arial",
        color="#30918E",
        width=650,
        text_align=ft.TextAlign.CENTER,
        #bgcolor="#913052"

    )

    #INTERFAZ
    page.add(
        #TEXTO
        ft.Text("Primera aplicacion",size=22,color=ft.colors.RED),
        nombre,
        boton,
        boton2,
        boton3,
        boton4,
        botonFlotante,
        boton5,
        botonIcono,
        texto
    )

#EJECUCION DEL PROYECTO
ft.app(main)
