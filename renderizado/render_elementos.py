import pygame
from datos.constantes import ANCHO, ALTO
import os
IMAGENES_CACHE = {}
_IMAGEN_CACHE = {}

LOGO = pygame.image.load("assets/images/icon_lol.png")
LOGO = pygame.transform.scale(LOGO, (300, 300))

FONDO = pygame.image.load("assets/images/jonia_fondo.jpg")
FONDO = pygame.transform.scale(FONDO,(ANCHO, ALTO) )

def logo_juego():
    return LOGO

def fondo_juego():
    return FONDO


def crear_button_rect(superficie, x, y, ancho, alto, texto, color_fondo, color_texto, tamano_fuente=24, tamaño_fuente=None):
    """
    Crear un botón y devolver su rect.
    Acepta tanto 'tamano_fuente' como 'tamaño_fuente' para compatibilidad.
    """
    # elegir el tamaño de fuente correcto (compatibilidad con ambos nombres)
    if tamaño_fuente is not None:
        tam = tamaño_fuente
    else:
        tam = tamano_fuente

    fuente = pygame.font.Font(None, tam)
    rectangulo = pygame.Rect(x, y, ancho, alto)

    # dibujar borde y fondo
    borde_color = (0, 0, 0)
    pygame.draw.rect(superficie, borde_color, rectangulo, border_radius=8)
    inner_rect = rectangulo.inflate(-4, -4)
    pygame.draw.rect(superficie, color_fondo, inner_rect, border_radius=8)

    texto_img = fuente.render(texto, True, color_texto)
    texto_x = inner_rect.x + (inner_rect.width - texto_img.get_width()) // 2
    texto_y = inner_rect.y + (inner_rect.height - texto_img.get_height()) // 2

    superficie.blit(texto_img, (texto_x, texto_y))
    return rectangulo


def precargar_imagenes_cartas(cartas):
    proyecto_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    for carta in cartas:
        ruta_rel = carta.get("imagen")
        if not ruta_rel:
            continue

        ruta_rel = os.path.normpath(ruta_rel)
        ruta_full = ruta_rel if os.path.isabs(ruta_rel) else os.path.normpath(os.path.join(proyecto_root, ruta_rel))

        if os.path.exists(ruta_full):
            img = pygame.image.load(ruta_full).convert_alpha()
            IMAGENES_CACHE[ruta_rel] = img


def obtener_imagen_por_ruta(ruta_rel, size=None):
    if not ruta_rel:
        return None

    if ruta_rel in _IMAGEN_CACHE:
        img = _IMAGEN_CACHE[ruta_rel]
        return pygame.transform.smoothscale(img, size) if img and size else img

    proyecto_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    ruta_full = ruta_rel if os.path.isabs(ruta_rel) else os.path.normpath(os.path.join(proyecto_root, ruta_rel))

    # debug: mostrar ruta y existencia
    print("DEBUG imagen -> ruta_rel:", ruta_rel, "ruta_full:", ruta_full, "exists:", os.path.exists(ruta_full))

    if not os.path.exists(ruta_full):
        _IMAGEN_CACHE[ruta_rel] = None
        return None

    # pygame must be initialized; cargar sin try/except
    img = pygame.image.load(ruta_full).convert_alpha()
    _IMAGEN_CACHE[ruta_rel] = img
    print("DEBUG imagen cargada y cacheada:", ruta_rel)
    return pygame.transform.smoothscale(img, size) if size else img