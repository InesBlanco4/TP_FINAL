import pygame

def cargar_cartas():
    carpeta_cartas = "imagenes/cartas/"
    valores_cartas = {
        "1 de espada": 14,
        "1 de basto": 13,
        "7 de espada": 12,
        "7 de oro": 11,
        "3 de espada": 10,
        "3 de basto": 10,
        "3 de oro": 10,
        "3 de copa": 10,
        "2 de espada": 9,
        "2 de basto": 9,
        "2 de oro": 9,
        "2 de copa": 9,
        "1 de oro": 8,
        "1 de copa": 8,
        "12 de espada": 7,
        "12 de basto": 7,
        "12 de oro": 7,
        "12 de copa": 7,
        "11 de espada": 6,
        "11 de basto": 6,
        "11 de oro": 6,
        "11 de copa": 6,
        "10 de espada": 5,
        "10 de basto": 5,
        "10 de oro": 5,
        "10 de copa": 5,
        "7 de copa": 4,
        "7 de basto": 3,
        "6 de espada": 2,
        "6 de basto": 2,
        "6 de oro": 2,
        "6 de copa": 2,
        "5 de espada": 1,
        "5 de basto": 1,
        "5 de oro": 1,
        "5 de copa": 1,
        "4 de espada": 0,
        "4 de basto": 0,
        "4 de oro": 0,
        "4 de copa": 0,
    }

    cartas = {}
    for nombre, valor in valores_cartas.items():
        ruta_imagen = f"{carpeta_cartas}{nombre}.jpg"
        try:
            imagen = pygame.image.load(ruta_imagen)
        except pygame.error:
            print(f"Error: No se encontró la imagen para {nombre}.")
            imagen = None 
        
        cartas[nombre] = {"valor": valor, "imagen": imagen}

    return cartas

# if __name__ == "__main__":

    pygame.init()
    cartas = cargar_cartas()
    for nombre, datos in cartas.items():
        print(f"{nombre}: Valor = {datos['valor']}, Imagen cargada = {datos['imagen'] is not None}")
    pygame.quit()