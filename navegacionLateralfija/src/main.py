import flet as ft #impotacion

def main(page: ft.Page): #funcion principál

    #PASO 1. DEFINIR LA VARIABLE NAVEGACION PARA CREAR EL OBJETO
    navegacion=ft.NavigationRail(
        min_width=150,
        destinations=[
            ft.NavigationRailDestination(
                label="Inicio",
                icon=ft.Icons.HOME
            ),
            ft.NavigationRailDestination(
                label="Facebook",
                icon=ft.Icons.FACEBOOK
            ),
            ft.NavigationRailDestination(
                label="Tiktok",
                icon=ft.Icons.TIKTOK
            ),
            ft.NavigationRailDestination(
                label="Perfil",
                icon=ft.Icons.PERSON_2
            )
        ],
        selected_index=0,
        #bgcolor=ft.Colors.BROWN
        leading=ft.Image(src="https://d1csarkz8obe9u.cloudfront.net/posterpreviews/construction-company-logo%2C-real-estate-logo-%28-design-template-10b40dd4d995ad60d9b68696f4854c36_screen.jpg?ts=1669056348",
                         width=150,
                         border_radius=50
                         )
    )
    
    page.add( #interfaz
       ft.Row(
           [
               navegacion,
               ft.VerticalDivider(width=1),
               ft.Column(
                   [
                       ft.Text("Pagina Principal")
                   ],
                   alignment=ft.MainAxisAlignment.START,
                   expand=True
               ),
           ],
           expand=True
       )
    )


ft.app(main)
