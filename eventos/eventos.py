import pygame
from audio.gestor_de_audio import cargar_efecto, reproducir_efecto, EFECTO_CLICK
from datos.constantes import KEYS

def gestionar_eventos(evento, pantalla_actual, botones):
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
    return pantalla_actual