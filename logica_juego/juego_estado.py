import random
from logica_juego.datos import cartas
from logica_juego.modulo_funciones import toggle_lock, tirar, reset_juego
import pygame

def crear_estado_juego(num_dados=5, max_intentos=3):
    """
    Crea y devuelve un nuevo estado de juego (diccionario).
    """
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
            estado["dados"][i] = random.randint(1, 6)   # usar random.randint explícito
    estado["intento"] += 1
    # debug: imprimir valores para verificar
    return True
    

def cartas_de_dados(estado):
    resultado = []
    for i in estado["dados"]:  
        if 1 <= i <= len(cartas):
            resultado.append(cartas[i-1]) 
        else:
            resultado.append(None) 
    return resultado