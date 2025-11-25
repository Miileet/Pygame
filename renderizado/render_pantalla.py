import pygame
from datos.constantes import ANCHO, ALTO, COLOR_TEXTO_OSCURO, COLOR_SECUNDARIO, COLOR_TEXTO_CLARO
from renderizado.render_elementos import logo_juego, fondo_juego, crear_button_rect


def pantalla_principal(pantalla, ETIQUETAS, KEYS):
    logo = logo_juego()
    fondo = fondo_juego()

    ancho_logo = logo.get_width()
    alto_logo = logo.get_height()

    x_logo = (ANCHO - ancho_logo)//2
    y_logo = 10

    ANCHO_BOTON = 130   
    ALTO_BOTON = 50     
    ESPACIO = 12

    total_ancho_botones = (ANCHO_BOTON  * 5) + (ESPACIO * 4)
    inicio_botones_x = (ANCHO- total_ancho_botones)//2
    y_botones = y_logo + logo.get_height()-20
    botones = []

    pantalla.blit(fondo, (0, 0))
    pantalla.blit(logo, (x_logo, y_logo))

    for i, texto in enumerate(ETIQUETAS):
        x = inicio_botones_x + i * (ANCHO_BOTON + ESPACIO)
        rect = crear_button_rect(pantalla,x, y_botones,ANCHO_BOTON, ALTO_BOTON,texto,COLOR_SECUNDARIO,COLOR_TEXTO_CLARO,tamaño_fuente=20)
        botones.append({"accion": KEYS[i], "rect": rect})

    return botones

def pantalla_opciones(pantalla):
    pantalla.fill((40, 40, 40))
    fuente_titulo = pygame.font.Font(None, 70)
    fuente_texto = pygame.font.Font(None, 40)
    texto_titulo = fuente_titulo.render("Opciones", True, COLOR_TEXTO_CLARO)
    pantalla.blit(texto_titulo, (ANCHO//2 - texto_titulo.get_width()//2, 50))
    botones = []
    rect_volver = crear_button_rect(pantalla, ANCHO//2 - 80, ALTO - 100, 
                                    160, 60, "Volver", COLOR_TEXTO_OSCURO, 
                                    COLOR_SECUNDARIO)
    botones.append({"accion": "menu", "rect": rect_volver})

    return botones


def pantalla_jugar(pantalla):
    fondo = fondo_juego()
    pantalla.blit(fondo, (0, 0))
    fuente_titulo = pygame.font.Font(None, 90)
    fuente_texto = pygame.font.Font(None, 50)