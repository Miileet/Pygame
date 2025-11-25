import pygame
import datos.constantes as con
from renderizado.render_pantalla import pantalla_principal, pantalla_jugar, pantalla_opciones
from eventos.eventos import gestionar_eventos
from audio.gestor_de_audio import reproducir_musica, MUSICA_MAIN
from datos.constantes import ETIQUETAS, KEYS
from logica_juego.juego_estado import crear_estado_juego, reset_juego, tirar, toggle_lock, cartas_de_dados

pygame.init()
pygame.mixer.init()
pantalla = pygame.display.set_mode((con.ANCHO, con.ALTO))
pygame.display.set_caption(con.TITULO)
reloj = pygame.time.Clock()
FPS = 60
pantalla_actual = "menu"
musica_actual = None
botones = None
ejecutando = True
estado_juego = crear_estado_juego()
primera_vez_jugar = True


while ejecutando:
    for evento in pygame.event.get():
        pantalla_actual = gestionar_eventos(evento, pantalla_actual, botones, estado_juego)

    if pantalla_actual == "menu":
        if musica_actual != "menu":
            reproducir_musica(MUSICA_MAIN)
            musica_actual = "menu"
        botones = pantalla_principal(pantalla, ETIQUETAS, KEYS)

    elif pantalla_actual == "jugar":
        if primera_vez_jugar:
            reset_juego(estado_juego)
            tirar(estado_juego)
            primera_vez_jugar = False
        botones = pantalla_jugar(pantalla, estado_juego)

    elif pantalla_actual == "opciones":
        botones = pantalla_opciones(pantalla)

    elif pantalla_actual == "creditos":
        botones = None

    elif pantalla_actual == "stats":
        botones = None

    elif pantalla_actual == "salir":
        ejecutando = False

    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()