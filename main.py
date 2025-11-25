import pygame
import datos.constantes as con
from renderizado.render_pantalla import pantalla_principal, pantalla_opciones
from eventos.eventos import gestionar_eventos
from audio.gestor_de_audio import reproducir_musica, MUSICA_MAIN
from datos.constantes import ETIQUETAS, KEYS
from logica_juego.modulo_funciones import jugar


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


while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        else:
            pantalla_actual = gestionar_eventos(evento, pantalla_actual, botones)
    if pantalla_actual == "menu":
        if musica_actual != "menu":
            reproducir_musica(MUSICA_MAIN)
            musica_actual = "menu"
        botones = pantalla_principal(pantalla, ETIQUETAS, KEYS)

    elif pantalla_actual == "jugar":
        botones = jugar()
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