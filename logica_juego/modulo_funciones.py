import random
from logica_juego.datos import cartas
from datos.constantes import ANCHO, ALTO, COLOR_TEXTO_CLARO, COLOR_SECUNDARIO, ITERACION_DADOS, INICIO_CARAS, FIN_CARAS
import pygame
from renderizado.render_elementos import fondo_juego, crear_button_rect

def mostrar_menu():
    print("\n==========Mini generala==========\n")
    print("Que desea hacer=\n1)Jugar\n2)Estadisticas\n3)Creditos\n4)Salir\n")

def tirar_dados():
    lista_dados = []

    for i in range(ITERACION_DADOS):
        lista_dados.append(random.randint(INICIO_CARAS, FIN_CARAS))
    return lista_dados

def mostrar_campeones(dados):
    print("\n==========CAMPEONES ACTUALES==========\n")
    carta_numero = 1
    for dado in dados:
        carta = cartas[dado-1] 
        print(f"({carta_numero}) - {carta['nombre']} ({carta['region']}) - Valor: {carta['puntos']}")
        carta_numero += 1


def conteo_de_valores(dados):
    conteo = {}
    for i in dados:
        if i in conteo:
            conteo[i] += 1
        else :
            conteo[i] = 1
    return conteo

def bubble_sort(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def jugadas(dados, conteo):
    valores = bubble_sort(list(conteo.values()))
    datos_ordenados = bubble_sort(dados)

    if 5 in valores:
        return "GENERALA", 50
    elif 4 in valores:
        return "POKER", 40
    elif valores == [2, 3]:
        return "FULL", 30
    elif es_escalera(datos_ordenados):
        return "ESCALERA", 20
    else:
        return "NADA", sum(dados)

def es_escalera(lista):
    for i in range(len(lista)-1):
        if lista[i+1] - lista[i] != 1:
            return False
    return True


def  creditos():
    print("\n----Creditos----")
    print("Desarrolladores: Romero Santiago y Nestor Zalazar")
    print("Profes: Martin Alejandro Garcia y Vero")
    print("Materia: Programacion I")
    print("Fecha de realizacion: Noviembre de 2025")
    print("Tematica: League of Legends")

def crear_planilla():
    return {
        "Unos": "-",
        "Doses": "-",
        "Treses": "-",
        "Cuatros": "-",
        "Cincos": "-",
        "Seises": "-",
        "Escalera": "-",
        "Full": "-",
        "Póker": "-",
        "Generala": "-"
    }

def mostrar_planilla(planilla):
    print("\n----- Planilla de puntajes ------")
    for categoria, valor in planilla.items():
        print(f"{categoria}: {valor}")

def crear_estado_juego(num_dados, max_intentos=3):

    return {
        "num_dados": num_dados,
        "max_intentos": max_intentos,
        "dados": [0] * num_dados,
        "locked": [False] * num_dados,
        "intento": 0
    }

def reset_juego(estado):
    estado["dados"] = [0] * estado["num_dados"]
    estado["locked"] = [False] * estado["num_dados"]
    estado["intento"] = 0

def tirar(estado):
    if estado["intento"] >= estado["max_intentos"]:
        return False
    
    for i in range(estado["num_dados"]):
        if not estado["locked"][i]:
            estado["dados"][i] = random.randint(1, 6)
    
    estado["intento"] += 1
    return True

def cartas_de_dados(estado):
    resultado = []
    for i in estado["dados"]:  
        if 1 <= i <= len(cartas):
            resultado.append(cartas[i-1]) 
        else:
            resultado.append(None) 
    return resultado

def toggle_lock(estado, idx):
    if 0 <= idx < estado["num_dados"] and estado["intento"] > 0:
        estado["locked"][idx] = not estado["locked"][idx]

def pantalla_jugar(pantalla, estado_juego):
    """
    Dibuja la pantalla de juego. Devuelve lista de botones {'accion','rect'}.
    """
    botones = []

    pantalla.fill((30, 30, 30))

    fuente_titulo = pygame.font.Font(None, 36)
    txt = fuente_titulo.render("Partida - Generala LOL", True, COLOR_TEXTO_CLARO)
    pantalla.blit(txt, ((ANCHO - txt.get_width()) // 2, 10))

    dados = estado_juego["dados"]
    locked = estado_juego["locked"]
    intento = estado_juego["intento"]

    DADO_W, DADO_H = 100, 120
    espacio = 15
    total_w = DADO_W * len(dados) + espacio * (len(dados) - 1)
    start_x = (ANCHO - total_w) // 2
    y = 80

    fuente_num = pygame.font.Font(None, 44)
    fuente_nombre = pygame.font.Font(None, 16)

    cartas_info = cartas_de_dados(estado_juego)

    for i, val in enumerate(dados):
        x = start_x + i * (DADO_W + espacio)
        rect = pygame.Rect(x, y, DADO_W, DADO_H)
        
        pygame.draw.rect(pantalla, (0, 0, 0), rect, border_radius=8)
        inner = rect.inflate(-6, -6)
        
        color_fondo = (200, 200, 200) if not locked[i] else (160, 120, 120)
        pygame.draw.rect(pantalla, color_fondo, inner, border_radius=8)

        num_text = fuente_num.render(str(val) if val else "-", True, (10, 10, 10))
        pantalla.blit(num_text, (inner.x + (inner.width - num_text.get_width()) // 2, 
                                 inner.y + (inner.height // 2 - num_text.get_height() // 2)))

        if cartas_info[i]:
            nombre = cartas_info[i]["nombre"]
            imagen_path = cartas_info[i].get("imagen", None)
            
            if imagen_path:
                imagen = pygame.image.load(imagen_path)
                imagen = pygame.transform.scale(imagen, (DADO_W - 12, 60))
                pantalla.blit(imagen, (inner.x + 3, inner.y + 30))
            else:
                nombre_txt = fuente_nombre.render(nombre, True, (10, 10, 10))
                pantalla.blit(nombre_txt, (inner.x + (inner.width - nombre_txt.get_width()) // 2, ))
        botones.append({"accion": f"lock_{i}", "rect": rect})

    BTN_W, BTN_H = 120, 40
    gap = 16
    bx = (ANCHO - (BTN_W * 3 + gap * 2)) // 2
    by = y + DADO_H + 40

    rect_tirar = crear_button_rect(pantalla, bx, by, BTN_W, BTN_H, botones.append({"accion": "tirar", "rect": rect_tirar}))

    rect_guardar = crear_button_rect(pantalla, bx + (BTN_W + gap), by, BTN_W, BTN_H, "Guardar",    botones.append({"accion": "guardar", "rect": rect_guardar}))

    rect_volver = crear_button_rect(pantalla, bx + 2 * (BTN_W + gap), by, BTN_W, BTN_H, "Volver",
                                    COLOR_SECUNDARIO, COLOR_TEXTO_CLARO, tamano_fuente=20)
    botones.append({"accion": "volver", "rect": rect_volver})

    return botones

def jugar():
    print("\n==========NUEVA PARTIDA==========\n")
    planilla = crear_planilla()
    puntaje_total = 0
    dados = tirar_dados()
    for intento in range(1,4):
        print(f"Tirada n: {intento}")
        mostrar_campeones(dados)
        
        if intento <= 3:
            opcion = input("\nQueres volver a tirar las cartas? (s/n)\n- - ->: ").lower()
            if opcion == "s":
                eleccion = input("Elegi los dados que queres volver a tirar (ejemplo: 1 3 2)\n- - ->: ")
                for posicion in eleccion.split():
                    if posicion.isdigit():
                        indice = int(posicion)-1
                        if 0 <= indice < ITERACION_DADOS: 
                            dados[indice] = random.randint(INICIO_CARAS, FIN_CARAS)
        else:
            break
    conteo = conteo_de_valores(dados)
    jugada, puntos = jugadas(dados, conteo)
    print(f"El resultado final es: {jugada} ({puntos} puntos)\n")

    mostrar_planilla(planilla)
    while True:
        categoria = input("Elija una categoria donde anotar los puntos\n- - ->: ").capitalize()
        if categoria in planilla and planilla[categoria] == "-":
            planilla[categoria] = puntos
            puntaje_total += puntos
            break
        else:
            print("Categoria invaldia o ya ingresada.")

    print("\n ----- Resultado final ------")
    mostrar_planilla(planilla)
    print(f"Puntaje total: {puntaje_total}")
    print("=====================================\n")
    input("Apreta enter para ir al menu")


