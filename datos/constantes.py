import datos.config_json as config_json

datos = config_json.cargar_datos()
ANCHO = datos["config"]["ventana"]["ancho"]
ALTO = datos["config"]["ventana"]["alto"]
COLOR_FONDO = datos["config"]["colores"]["fondo"]
TITULO = datos["config"]["ventana"]["titulo"]
COLOR_TEXTO_OSCURO = datos["config"]["colores"]["texto_oscuro"]
COLOR_TEXTO_CLARO = datos["config"]["colores"]["texto_claro"]
COLOR_SECUNDARIO =  datos["config"]["colores"]["primario"]
VOLUMEN = datos["config"]["audio"]["volumen"]
ETIQUETAS = ["Jugar", "Opciones", "Creditos", "Stats", "Salir"]
KEYS = ["jugar", "opciones", "creditos", "stats", "salir"]