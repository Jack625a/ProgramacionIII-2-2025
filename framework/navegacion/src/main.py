import flet as ft

def main(page: ft.Page):

    #PASO 1. CREAR LA NAVEGACION
    page.navigation_bar=ft.NavigationBar(
        #PASO 2. CREAR LAS OPCIONES DE LA NAVEGACION
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME,label="Inicio",),
            ft.NavigationBarDestination(icon=ft.Icons.SHOP, label="Productos"),
            ft.NavigationBarDestination(icon=ft.Icons.SKATEBOARDING,label="Servicios"),
            ft.NavigationBarDestination(icon=ft.Icons.TIKTOK, label="Contactos"),
            ft.NavigationBarDestination(icon=ft.Icons.ACCOUNT_BOX_SHARP, label="Redes")
        ],
        bgcolor=ft.Colors.YELLOW_200,
        indicator_color=ft.Colors.YELLOW_800,
        surface_tint_color=ft.Colors.WHITE
    )
    #NAVEGACION 2- NAVEGACION LATERAL
    #PASO1. DEFINIR LA NAVEGACION
    navegacionLateral=ft.NavigationDrawer(
        controls=[
            ft.NavigationDrawerDestination(icon=ft.Icons.FACEBOOK,label="Facebook"),
            ft.NavigationDrawerDestination(icon=ft.Icons.GPS_FIXED,label="Ubicacion"),
            ft.NavigationDrawerDestination(icon=ft.Icons.TIKTOK, label="Tiktok")

        ],
        bgcolor=ft.Colors.BLUE_400,
    )
    #page.open(navegacionLateral)
    page.add(
        ft.ElevatedButton(text="Mostrar",on_click=lambda e:page.open(navegacionLateral))
    )


ft.app(main)
