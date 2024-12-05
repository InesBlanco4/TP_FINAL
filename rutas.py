ruta_actual = "menu"
rutas_validas = ["menu", "jugar", "opciones", "creditos"]

def navegar(ruta: str):
    global ruta_actual
    if ruta in rutas_validas:
        ruta_actual = ruta
