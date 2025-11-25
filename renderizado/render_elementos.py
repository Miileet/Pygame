import pygame
from datos.constantes import ANCHO, ALTO

LOGO = pygame.image.load("assets/images/icon_lol.png")
LOGO = pygame.transform.scale(LOGO, (300, 300))

FONDO = pygame.image.load("assets/images/jonia_fondo.jpg")
FONDO = pygame.transform.scale(FONDO,(ANCHO, ALTO) )

def logo_juego():
    return LOGO

def fondo_juego():
    return FONDO


def crear_button_rect(superficie, x, y, ancho, alto, texto, color_fondo, color_texto, tamaño_fuente=24):
    fuente = pygame.font.Font(None, tamaño_fuente)
    rectangulo = pygame.Rect(x, y, ancho, alto)
    borde_color = (0, 0, 0)
    pygame.draw.rect(superficie, borde_color, rectangulo, border_radius=8)
    inner_rect = rectangulo.inflate(-4, -4)
    pygame.draw.rect(superficie, color_fondo, inner_rect, border_radius=8)
    texto_img = fuente.render(texto, True, color_texto)
    texto_x = inner_rect.x + (inner_rect.width - texto_img.get_width())//2
    texto_y = inner_rect.y + (inner_rect.height - texto_img.get_height())//2
    superficie.blit(texto_img, (texto_x, texto_y))
    return rectangulo