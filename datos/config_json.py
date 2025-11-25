import json
import os

config_default = {
    "config": {
        "ventana": {"ancho": 800, "alto": 600, "titulo": "Generala LOL"},
        "audio": {"volumen": 0.2},
        "colores": {
            "fondo": [135, 62, 99],
            "primario": [30, 30, 30],      
            "secundario": [60, 60, 60],    
            "texto_claro": [255, 255, 255],
            "texto_oscuro": [10, 10, 10]
        }
    }}

archivo_config = "config.json"

def guardar_datos(datos):
    with open(archivo_config, "w") as archivo:
        json.dump(datos, archivo, indent=4)

def cargar_datos():
    if not os.path.exists(archivo_config) or os.path.getsize(archivo_config) == 0:
        guardar_datos(config_default)
        return config_default

    with open(archivo_config, "r") as archivo:
        datos = json.load(archivo)
    if "config" not in datos:
        guardar_datos(config_default)
        return config_default
    return datos