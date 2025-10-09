import flet as ft

def contenidoPantalla2():
    
    return ft.Container(
        content=ft.Card(
            content=ft.Column(
                controls=[
                    ft.Text("Contenedor Card"),
                    ft.Text("Contenido"),
                    ft.Text("Acciones"),
                    ft.Image(src="https://picsum.photos/150/150/?87", width=150)
                ]
            ),width=300,
            shadow_color=ft.Colors.ON_INVERSE_SURFACE
        ),bgcolor=ft.Colors.GREEN_400
    
    )
   
    


#ft.Card(
 #       content=ft.Container(
  #          content=(
   #             ft.Text("Contenedor Card")
    #        )
     #   )

    #)
    