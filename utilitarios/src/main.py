import flet as ft #importacion
import os

def main(page: ft.Page): #funcion principal
    rutaAudio=os.path.join(os.getcwd(),"assets","audio.mp3")
    #PASO 1. DEFINIR LA VARIABLE AUDIO
    audio=ft.Audio(
        src="https://luan.xyz/files/audio/ambient_c_motion.mp3", #direccion del audio
        autoplay=True
    )
    page.overlay.append(audio)

    botonPausa=ft.ElevatedButton("Pausar", on_click=lambda _: audio.pause())
    botonPlay=ft.ElevatedButton("Play",on_click=lambda _: audio.play())

    page.add( #interfaz
        botonPlay,botonPausa
    )

ft.app(main)
