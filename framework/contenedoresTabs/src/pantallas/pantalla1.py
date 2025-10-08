import flet as ft

def contenidoPantalla1():
    listaDatos=[]
    for fotos in range(0,100):
        listaDatos.append(
            f"https://picsum.photos/150/150/?{fotos}"
        )

    print(listaDatos)
    #CONTENEDOR TIPO GRID (FILAS,COLUMNAS)
    datos=ft.GridView(
            spacing=5,
            expand=1,
            max_extent=150,
            run_spacing=10,
            controls=(
                ft.Image(
                src=f"https://picsum.photos/150/150?",
            ),
             ft.Image(
                src=f"https://picsum.photos/150/150?",
            ),
             ft.Image(
                src=f"https://picsum.photos/150/150?",
            ), ft.Image(
                src=f"https://picsum.photos/150/150?",
            ), ft.Image(
                src=f"https://picsum.photos/150/150?",
            ), ft.Image(
                src=f"https://picsum.photos/150/150?",
            )
    )
    )
    


    return ft.Container(  
        content=datos
        )