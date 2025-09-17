#IMPORTACION DEL FRAMEWORK
import flet as ft

#FUNCION PRINCIPAL 
def main(page: ft.Page):
    
    nombre=ft.Text("Kevin Arroyo Montaño", size=25)
    boton=ft.Button("Prueba Boton",bgcolor=ft.colors.GREEN_400)

    #INTERFAZ
    page.add(
        #TEXTO
        ft.Text("Primera aplicacion",size=22,color=ft.colors.RED),
        nombre,
        boton
    )

#EJECUCION DEL PROYECTO
ft.app(main)
