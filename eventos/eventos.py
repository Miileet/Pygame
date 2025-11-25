import pygame
from audio.gestor_de_audio import cargar_efecto, reproducir_efecto, EFECTO_CLICK
from datos.constantes import KEYS
from logica_juego.juego_estado import tirar, toggle_lock

def gestionar_eventos(evento, pantalla_actual, botones, estado_juego=None):
    if evento.type == pygame.QUIT:
        return "salir"

    if botones is None:
        return pantalla_actual

    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        pos = pygame.mouse.get_pos()
        for boton in botones:
            if boton["rect"].collidepoint(pos):
                efecto = cargar_efecto(EFECTO_CLICK)
                reproducir_efecto(efecto)
                accion = boton["accion"]

                if pantalla_actual == "menu" and accion in KEYS:
                    return accion

                if pantalla_actual == "jugar" and estado_juego is not None:
                    if accion == "tirar":
                        tirar(estado_juego)
                        return "jugar"
                    if accion == "guardar":
                        return "menu"
                    if accion == "volver":
                        return "menu"
                    if accion.startswith("lock_"):
                        idx = int(accion.split("_")[1])
                        toggle_lock(estado_juego, idx)
                        return "jugar"

                if accion == "salir":
                    return "salir"
                if accion == "creditos":
                    return "creditos"
                if accion == "stats":
                    return "stats"
                if accion == "jugar":
                    return "jugar"

    return pantalla_actual