import random
from logica_juego.datos import cartas
from logica_juego.constantes import *

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


