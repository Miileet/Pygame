import pygame
from datos.constantes import ANCHO, ALTO, COLOR_TEXTO_OSCURO, COLOR_SECUNDARIO, COLOR_TEXTO_CLARO
from renderizado.render_elementos import logo_juego, fondo_juego, crear_button_rect
from logica_juego.juego_estado import cartas_de_dados

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


def pantalla_jugar(pantalla, estado_juego):
    fondo = fondo_juego()
    pantalla.blit(fondo, (0, 0))
    fuente_titulo = pygame.font.Font(None, 90)
    fuente_texto = pygame.font.Font(None, 50)


def pantalla_jugar(pantalla, estado_juego):
    """
    Dibuja la pantalla de juego. Devuelve lista de botones {'accion','rect'}.
    """
    botones = []

    # dibujar fondo
    pantalla.fill((30, 30, 30))

    # título
    fuente_titulo = pygame.font.Font(None, 36)
    txt = fuente_titulo.render("Partida - Generala LOL", True, COLOR_TEXTO_CLARO)
    pantalla.blit(txt, ((ANCHO - txt.get_width()) // 2, 10))

    dados = estado_juego["dados"]
    locked = estado_juego["locked"]
    intento = estado_juego["intento"]

    # configuración visual dados
    DADO_W, DADO_H = 100, 140
    espacio = 12
    total_w = DADO_W * len(dados) + espacio * (len(dados) - 1)
    start_x = (ANCHO - total_w) // 2
    y = 70

    fuente_num = pygame.font.Font(None, 48)
    fuente_nombre = pygame.font.Font(None, 14)

    cartas_info = cartas_de_dados(estado_juego)

    for i, val in enumerate(dados):
        x = start_x + i * (DADO_W + espacio)
        rect = pygame.Rect(x, y, DADO_W, DADO_H)
        
        # borde negro
        pygame.draw.rect(pantalla, (0, 0, 0), rect, border_radius=8)
        inner = rect.inflate(-6, -6)
        
        # color según si está bloqueado
        color_fondo = (200, 200, 200) if not locked[i] else (160, 100, 100)
        pygame.draw.rect(pantalla, color_fondo, inner, border_radius=8)

        # número del dado (grande)
        if val > 0:
            num_text = fuente_num.render(str(val), True, (10, 10, 10))
            pantalla.blit(num_text, (inner.x + (inner.width - num_text.get_width()) // 2, inner.y + 10))
        else:
            num_text = fuente_num.render("?", True, (100, 100, 100))
            pantalla.blit(num_text, (inner.x + (inner.width - num_text.get_width()) // 2, inner.y + 10))

        # nombre de la carta debajo
        if cartas_info[i]:
            nombre = cartas_info[i]["nombre"]
            nombre_txt = fuente_nombre.render(nombre, True, (10, 10, 10))
            pantalla.blit(nombre_txt, (inner.x + (inner.width - nombre_txt.get_width()) // 2, inner.y + inner.height - 25))

        botones.append({"accion": f"lock_{i}", "rect": rect})

    # información de intento
    fuente_info = pygame.font.Font(None, 24)
    info_txt = fuente_info.render(f"Intento: {intento}/{estado_juego['max_intentos']}", True, COLOR_TEXTO_CLARO)
    pantalla.blit(info_txt, (20, y + DADO_H + 20))

    # botones de control
    BTN_W, BTN_H = 110, 40
    gap = 12
    bx = (ANCHO - (BTN_W * 3 + gap * 2)) // 2
    by = y + DADO_H + 60

    rect_tirar = crear_button_rect(pantalla, bx, by, BTN_W, BTN_H, "Tirar",COLOR_SECUNDARIO, COLOR_TEXTO_CLARO, tamano_fuente=18)
    botones.append({"accion": "tirar", "rect": rect_tirar})

    rect_guardar = crear_button_rect(pantalla, bx + (BTN_W + gap), by, BTN_W, BTN_H, "Guardar",COLOR_SECUNDARIO, COLOR_TEXTO_CLARO, tamano_fuente=18)
    botones.append({"accion": "guardar", "rect": rect_guardar})

    rect_volver = crear_button_rect(pantalla, bx + 2 * (BTN_W + gap), by, BTN_W, BTN_H, "Volver",
                                    COLOR_SECUNDARIO, COLOR_TEXTO_CLARO, tamano_fuente=18)
    botones.append({"accion": "volver", "rect": rect_volver})

    return botones